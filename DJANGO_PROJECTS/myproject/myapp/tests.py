from django.test import TestCase
from .models import Article
from django.urls import reverse

class ArticleTests(TestCase):

    def test_article_creation(self):
        article = Article.objects.create(title="Test Article", content="This is a test article")
        self.assertEqual(article.title, "Test Article")
        self.assertEqual(article.content, "This is a test article")

    def test_article_create_view(self):
        response = self.client.get(reverse('article-create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create Article")
        self.assertTemplateUsed(response, 'article_form.html')
