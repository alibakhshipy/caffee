from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_cofe, name='shop_cofe'),
]