
from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register(r'companies', CompanyViewSet, base_name='company')
router.register(r'shop', ShopViewSet, base_name='shop')
router.register(r'product', ProductViewSet, base_name='product')

v1 = [
    url(r'^private/', include(router.urls)),
]
urlpatterns = [
    url(r'^v1/', include(v1))
]