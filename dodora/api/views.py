from datetime import datetime

from django.shortcuts import render

from rest_framework import viewsets, mixins
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status

from .serializer import *
from .models import *


class ProductViewSet(viewsets.ModelViewSet):
    """List services provided by company """
    queryset = Product.objects.all().order_by("pk")
    serializer_class = ProductSerializer


#class CustomerViewSet(viewsets.ModelViewSet):
 #   """Create, update, retrieve, delete Customer"""
  #  queryset = Customer.objects.all().order_by("pk")
   # serializer_class = CustomerSerializer


class ShopViewSet(viewsets.ModelViewSet):
    """Create, update, retrieve, delete Salon"""
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()


class CompanyViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()



# Create your views here.
