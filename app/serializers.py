from rest_framework import serializers

from .models import Category, OrderItems, Order, Pet


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    breed_name = serializers.CharField()


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    category = CategorySerializer()
    name = serializers.CharField()
    born_date = serializers.DateField()
    price = serializers.FloatField()
    quantity = serializers.IntegerField()
    gender = serializers.CharField()


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
