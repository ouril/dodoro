from .models import *
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

   class Meta:
       model = Product
       fields = '__all__'


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



