from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apis import CategoryApi, PetApi

router = DefaultRouter()
router.register("category", CategoryApi, basename="category")
router.register("pet", PetApi, basename="pet")
urlpatterns = [path("", include(router.urls))]
