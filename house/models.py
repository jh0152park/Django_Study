from django.db import models


# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=128)
    pet_allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
