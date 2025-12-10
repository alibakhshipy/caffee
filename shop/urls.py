from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_basket, name='user_basket'),
    path('remove/<int:detail_id>/', views.remove_from_cart, name='remove_from_cart'),
]