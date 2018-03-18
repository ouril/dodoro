"""dodora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from api.urls import urlpatterns as api_urls
from rest_framework_jwt.views import refresh_jwt_token
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'api-token-refresh/', refresh_jwt_token),
    url(r'^api/', include(api_urls)),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False))
]
