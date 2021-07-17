from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apis import CategoryApi, PetApi, OrderApi

router = DefaultRouter()
router.register("category", CategoryApi, basename="category")
router.register("pet", PetApi, basename="pet")
router.register("order", OrderApi, basename="order")
urlpatterns = [path("", include(router.urls))]
