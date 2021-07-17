from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.functional import cached_property


class Order(models.Model):
    code = models.CharField(max_length=255, unique=True, null=True)
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="user_orders", null=True
    )
    address_one = models.CharField(max_length=255)
    address_two = models.CharField(max_length=255, default="")
    phone_number = PhoneNumberField()
    email = models.EmailField()
    currency = models.CharField(max_length=50, default="USD")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.code = self.auto_generate_code()
        super().save(*args, **kwargs)

    def auto_generate_code(self):
        import hashlib
        import uuid

        orders_no = Order.objects.all().count()
        string_to_hash = f"{self.customer or (orders_no * -1)}.{orders_no}"
        code = f"#{hashlib.sha256(str.encode(string_to_hash + uuid.uuid4().hex)).hexdigest()[:8]}"
        return code

    @cached_property
    def total_price(self):
        from django.db.models import Sum, F

        return self.order_items.aggregate(total_price=Sum(F("quantity") * F("price")))[
            "total_price"
        ]

    def add_items(self, items):
        from django.shortcuts import get_object_or_404
        from .pet import Pet

        for item in items:
            OrderItems.objects.create(
                order=self,
                dog=get_object_or_404(Pet, pk=item["pet"]),
                quantity=item["quantity"],
            )


class OrderItems(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    dog = models.ForeignKey(
        "app.Pet", on_delete=models.PROTECT, related_name="user_orders"
    )
    price = models.FloatField(default=0)
    quantity = models.IntegerField()

    def save(self, *args, **kwargs):
        self.price = self.dog.price
        if not self.dog.quantity >= self.quantity:
            from rest_framework.validators import ValidationError

            raise ValidationError()
        self.dog.quantity -= self.quantity
        self.dog.save(update_fields=["quantity"])
        super().save(*args, **kwargs)

    @cached_property
    def total_item_price(self):
        return self.price * self.quantity
