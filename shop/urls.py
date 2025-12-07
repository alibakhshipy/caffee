from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_basket, name='user_basket'),
]