# books/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Book

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a book
        cls.book = Book.objects.create(
            title='Sample Book Title',
            author='Sample Author',
            description='Sample Description',
            published_date='2023-10-26',
            price=19.99,
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, 'Sample Book Title')
        self.assertEqual(self.book.author, 'Sample Author')
        self.assertEqual(self.book.description, 'Sample Description')
        self.assertEqual(self.book.published_date, '2023-10-26')
        self.assertEqual(self.book.price, 19.99)

    def test_book_retrieval(self):
        book_from_db = Book.objects.get(id=self.book.id)
        self.assertEqual(book_from_db, self.book)

    def test_book_update(self):
        self.book.title = "An updated title"
        self.book.save()
        updated_book = Book.objects.get(id=self.book.id)
        self.assertEqual(updated_book.title, "An updated title")

    def test_book_deletion(self):
        book_id = self.book.id
        self.book.delete()
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=book_id)

    def test_permission(self):
        user_without_permission = User.objects.create_user(
            username='restricted_user',
            password='password123'
        )
        self.client.force_login(user_without_permission)
        
        response = self.client.post(
            reverse('books:book_update', args=[self.book.id]),
            data={
                'title': 'Updated Title',
                'author': 'Updated Author',
            }
        )

        self.assertEqual(response.status_code, 403)  # Ensure it's forbidden
