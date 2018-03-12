import os.path
import uuid
from decimal import Decimal
from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models

from rest_framework.exceptions import ValidationError
from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField

from django.conf import settings


class ABSComercia(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name="Name", unique=True)
    description = models.TextField(verbose_name="Description", blank=True, default="")

    def __str__(self):
        return self.name


class Company(ABSComercia):
    # TODO: add upload_path
    logo = models.ImageField(null=True, verbose_name="logo")
    is_active = models.BooleanField(verbose_name="Is active", default=False)


class Shop(ABSComercia):
    # TODO: add upload path
    logo = models.ImageField()
    is_opened = models.BooleanField(verbose_name="Is shop open", default=True)
    company = models.ForeignKey(
        Company,
        related_name="shop",
        verbose_name="Company",
        on_delete=models.CASCADE
    )


class Category(ABSComercia):
    pass


class Unit(ABSComercia):
    pass


class ProductType(ABSComercia):
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING)
    min_package = models.IntegerField(default=1, verbose_name="Minimum in package")


class Product(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=255, verbose_name="Product name")
    info = models.TextField(verbose_name='Discription of product', blank=True)
    company = models.ForeignKey(
        Company,
        related_name="product",
        verbose_name="Company",
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        verbose_name="Category",
        on_delete=models.DO_NOTHING
    )
    product_type = models.ForeignKey(
        ProductType,
        verbose_name="type of product",
        on_delete=models.DO_NOTHING
    )
    article = models.CharField(max_length=8, default="")

    def __str__(self):
        return self.name

    def set_article(self):
        # TODO: create function to build article
        self.article = str(self.id)[::5]
        return self.article


class Store(TimeStampedModel):
    shop = models.ForeignKey(
        Shop,
        verbose_name="Shop",
        related_name="store",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, verbose_name="Product", related_name="store")
    stock = models.PositiveIntegerField(verbose_name="Stock", default=0, null=True)

    def __str__(self):
        return "Shop {} store".format(self.shop.name)


class ShopContacts(TimeStampedModel):
    shop = models.ForeignKey(
        Shop,
        related_name="contacts",
        verbose_name="Shop",
        on_delete=models.CASCADE
    )
    addr = models.CharField(max_length=255, verbose_name="contacts")
    phone = PhoneNumberField()
    email = models.EmailField()
    # TODO: Add params


class Price(TimeStampedModel):
    product = models.ForeignKey(Product, related_name="price")
    money = MoneyField()
    # TODO: Finish with deferent money


class Customer(AbstractUser):
    phone = PhoneNumberField(verbose_name='Customer number', unique=True)


class Rating(TimeStampedModel):
    horribly = 1
    bad = 2
    tolerably = 3
    good = 4
    wonderful = 5
    RATING = (
        (horribly, 1),
        (bad, 2),
        (tolerably, 3),
        (good, 4),
        (wonderful, 5)
    )

    rating = models.SmallIntegerField(choices=RATING, verbose_name="rating")
    customer = models.ForeignKey(
        Customer,
        related_name="product_rating",
        verbose_name="Customer",
        on_delete=models.CASCADE

    )


class ProductRating(Rating):
    product = models.ForeignKey(
        Product,
        related_name="rating",
        verbose_name="Product",
        on_delete=models.CASCADE
    )


class ShopRating(Rating):
    shop = models.ForeignKey(
        Shop,
        related_name="rating",
        verbose_name="Shop",
        on_delete=models.CASCADE
    )


