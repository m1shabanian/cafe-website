from rest_framework import serializers

from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            "image",
            "category",
            "sugar",
            "coffee",
            "flour",
            "chocolate",
            "egg",
            "vertical"
            "price",
            "get_image",
        )


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "name",
            "image",
            "get_absolute_url",
            "products",
        )