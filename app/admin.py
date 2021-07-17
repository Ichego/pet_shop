from django.contrib import admin
from .models import Pet, Category, OrderItems, Order

# Register your models here.
admin.site.register(Pet)
admin.site.register(Category)
admin.site.register(OrderItems)
admin.site.register(Order)
