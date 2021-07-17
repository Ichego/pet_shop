from django.db import models


# Create your models here.
class Category(models.Model):
    breed_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.breed_name or self.pk}"
