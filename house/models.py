from django.db import models


# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=128)
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price", help_text="Postive Number Only"
    )
    description = models.TextField()
    address = models.CharField(max_length=128)
    pet_allowed = models.BooleanField(
        default=False,
        verbose_name="Pets Allowed?",
        help_text="This house allows pets?"
    )
    # unique key not a just simple integer
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
