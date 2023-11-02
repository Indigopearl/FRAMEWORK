from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    date_planted = models.DateField()

    def __str__(self):
        return self.name
