from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    stock = models.PositiveBigIntegerField()
