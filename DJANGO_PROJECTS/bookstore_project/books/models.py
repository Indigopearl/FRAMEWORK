# books/models.py
from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
