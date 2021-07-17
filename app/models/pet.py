from django.db import models


# Create your models here.
class Pet(models.Model):
    FEMALE = "F"
    MALE = "M"
    gender_choices = ((FEMALE, FEMALE), (MALE, MALE))
    category = models.ForeignKey(
        "app.Category", on_delete=models.PROTECT, related_name="category_pets"
    )
    name = models.CharField(max_length=50, unique=True)
    born_date = models.DateField()
    price = models.FloatField(default=100)
    quantity = models.IntegerField(default=1)
    gender = models.CharField(max_length=5, choices=gender_choices)

    class Meta:
        ordering = ["-born_date"]

    def __str__(self):
        return f"{self.category.breed_name} - {self.name}"

    @property
    def age(self):
        from datetime import datetime

        return (datetime.now().date() - self.born_date).days
