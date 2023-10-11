from django.test import TestCase
from django.urls import reverse

from . import views


class HomeViewTestCase(TestCase):
    def test_home_view_is_accessible(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_view_has_correct_message(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Welcome to the homepage!", html=True)

    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")


class AboutViewTestCase(TestCase):
    def test_about_view_is_accessible(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_about_view_has_correct_message(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "About us page.", html=True)

    def test_about_view_uses_correct_template(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
