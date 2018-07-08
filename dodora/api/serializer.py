from .models import (
    Product,
    Shop,
    ShopRating,
    Company,
    Customer,
    ProductRating,
    Category,
    ProductImage


)
from rest_framework import serializers


class CategorySerializer(serializers. ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = '__all__'


class ShopRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopRating
        fields = '__all__'


class ProductRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductRating
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"


class ImageProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    product_image = ImageProductSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'