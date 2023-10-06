from django.db import models

class AbstractUser(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100, null=True)

    class Meta:
        abstract = True

class AbstractAuthor(models.Model):
    followers = models.ManyToManyField('User', related_name='followed_authors')
    join_date = models.DateField()
    popularity_score = models.IntegerField()

    class Meta:
        abstract = True
