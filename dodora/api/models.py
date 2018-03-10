import os.path
import uuid
from decimal import Decimal
from datetime import timedelta

from django.db import models

from rest_framework.exceptions import ValidationError
from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField

from django.db import models


class ABSComercia(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name="Name", unique=True)
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.name


class Company(ABSComercia):
    # logo ???
    pass


class Shop(ABSComercia):
    # logo ???
    company = models.ForeignKey(Company, related_name="shop", verbose_name="Company")


class Product(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=255, verbose_name="Product name")
    info = models.TextField(verbose_name='Discription of product', blank=True)
    company = models.ForeignKey(Company, related_name="product", verbose_name="Company")

    @property
    def article(self):
        # TODO: create function to build article
        return self.id[:8]


class Store(TimeStampedModel):
    shop = models.ForeignKey(Shop, verbose_name="Shop", related_name="store")
    product = models.ForeignKey(Product, verbose_name="Product", related_name="store")
    stock = models.PositiveIntegerField(verbose_name="Stock", default=0, null=True)


class ShopContacts(TimeStampedModel):
    pass


class ProductCategory(models.Model):
    pass


class ProductType(models.Model):
    # TODO: build types with count by
    pass


class Price(TimeStampedModel):
    product = models.ForeignKey(Product, related_name="price")
    money = MoneyField()
    # TODO: Finish with deferent money


class Customer(TimeStampedModel):
    pass


class ProductRating(TimeStampedModel):
    pass


class ShopRating(TimeStampedModel):
    pass


