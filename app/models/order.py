from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.functional import cached_property


class Order(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="user_orders", null=True
    )
    address_one = models.CharField(max_length=255)
    address_two = models.CharField(max_length=255, default="")
    phone_number = PhoneNumberField()
    email = models.EmailField()
    currency = models.CharField(max_length=50, default="USD")

    @cached_property
    def total_price(self):
        from django.db.models import Sum, F

        return self.order_items.aggregate(total_price=Sum(F("quantity") * F("price")))[
            "total_price"
        ]


class OrderItems(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    dog = models.ForeignKey(
        "app.Pet", on_delete=models.PROTECT, related_name="user_orders"
    )
    price = models.FloatField()
    quantity = models.IntegerField()

    @cached_property
    def total_item_price(self):
        return self.price * self.quantity
