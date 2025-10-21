from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index_pageView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
]