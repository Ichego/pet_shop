from django.test import TestCase
from rest_framework.test import APIClient
from .models import Pet, Category, Order


class TestPetAppApi(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def add_category(self):
        Category.objects.get_or_create(breed_name="German Shepherd")
        Category.objects.get_or_create(breed_name="Golden Retriever")

    def add_pet(self):
        pet_dict = [
            {
                "category": Category.objects.first(),
                "name": "test dog",
                "born_date": "2021-07-16",
                "price": 100.0,
                "quantity": 10,
                "gender": "10",
            },
            {
                "category": Category.objects.last(),
                "name": "test dog 2 ",
                "born_date": "2021-07-16",
                "price": 150.0,
                "quantity": 10,
                "gender": "10",
            },
        ]
        Pet.objects.get_or_create(**pet_dict[0])
        Pet.objects.get_or_create(**pet_dict[1])

    def test_categories(self) -> None:
        self.add_category()
        response = self.client.get("/api/v1/category/")
        assert response.status_code == 200
        assert len(response.data) == Category.objects.count()
        assert response.data[0].get("breed_name") == "German Shepherd"

        self.add_pet()
        response = self.client.get("/api/v1/category/1/")
        assert response.status_code == 200
        assert len(response.data) == Pet.objects.filter(category_id=1).count()
        assert response.data[0].get("name") == "test dog"

    def test_pets(self) -> None:
        self.add_category()
        self.add_pet()

        response = self.client.get("/api/v1/pet/")
        assert response.status_code == 200
        assert len(response.data) == Pet.objects.count()
        assert response.data[0].get("name") == "test dog"

        response = self.client.get("/api/v1/pet/1/")
        assert response.status_code == 200
        assert response.data.get("name") == "test dog"

    def test_orders(self) -> None:
        order_json = {
            "address_one": "this is test order address",
            "phone_number": "+201116090444",
            "email": "a@a.com",
            "currency": "USD",
            "order_items": [{"pet": 1, "quantity": 2}, {"pet": 2, "quantity": 2}],
        }

        self.add_category()
        self.add_pet()
        response = self.client.post("/api/v1/order/", data=order_json, format="json")
        assert response.status_code == 200
        assert response.data.get("code") == Order.objects.last().code
        assert response.data.get("order_items")[0].get("total_item_price") == 200.0
        assert response.data.get("total_price") == 500.0
        assert Pet.objects.get(pk=1).quantity == 8
        order_json = {
            "address_one": "this is test order address",
            "phone_number": "+201116090444",
            "email": "a@a.com",
            "currency": "USD",
            "order_items": [{"pet": 1, "quantity": 12}],
        }
        response = self.client.post("/api/v1/order/", data=order_json, format="json")
        assert response.status_code == 422
