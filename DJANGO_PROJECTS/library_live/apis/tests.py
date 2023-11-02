from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="created during setup",
            subtitle="subtitle",
            author="W. Vincent",
            isbn="1234567890"
        )

    def test_api_listview(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        Book.objects.create(
            title="created during test",
            subtitle="subtitle",
            author="W. Vincent",
            isbn="1234567890"
        )
        print('First test: ' ,Book.objects.all())
        # self.assertEqual(len(Book.objects.all()), 1)
        self.assertContains(response, self.book)

    def test_api_listview2(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        print('Second Test: ', Book.objects.all())
        # self.assertEqual(len(Book.objects.all()), 1)
        self.assertContains(response, self.book)