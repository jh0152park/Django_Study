from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField()
    description = models.TextField()
    adress = models.CharField(max_length=128)