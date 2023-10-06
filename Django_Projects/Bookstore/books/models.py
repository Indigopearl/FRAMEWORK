from django.db import models
from .abstract_models import AbstractUser, AbstractAuthor


class Author(AbstractAuthor):
    # Fields specific to Author
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True)
    zip_code = models.IntegerField(null=True)
    telephone = models.CharField(max_length=100, null=True)
    join_date = models.DateField()
    popularity_score = models.IntegerField()


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=200)
    join_date = models.DateField()
    popularity_score = models.IntegerField()


class User(AbstractUser):
    # Fields specific to User
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100, null=True)


class Genre(models.Model):
    name = models.CharField(max_length=150)


class Books(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-published_date', 'price']
