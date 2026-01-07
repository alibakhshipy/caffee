from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.api_list_view, name='api_list'),
    path('<int:id>/', views.api_detail_view, name='api_detail')
]