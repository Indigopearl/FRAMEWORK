from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    genre = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    director = models.CharField(max_length=100)
    description = models.TextField()