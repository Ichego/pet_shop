"""
Apis for all project from showing products (Pets)
to Buying (Creating Order)
"""
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Category, Pet
from .serializers import CategorySerializer, PetSerializer


class CategoryApi(GenericViewSet, ListAPIView, RetrieveAPIView):
    """
    This Api for getting and retrieving Category.
    we are using caching on list every one hour to make response faster
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @method_decorator(cache_page(60 * 60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        writing custom retrieve
        using PetSerializer instead of CategorySerializer
        get all related Pets using related_name
        """
        return Response(
            PetSerializer(
                self.queryset.get(pk=kwargs.get("pk")).category_pets.all(), many=True
            ).data
        )


class PetApi(GenericViewSet, ListAPIView, RetrieveAPIView):
    """
    This Api for getting and retrieving Pets.
    we can filter it using category id as query parameter
    we are using caching on list every one hour to make response faster
    """

    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]

    @method_decorator(cache_page(60 * 60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
