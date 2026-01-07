from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Index_pageView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('api/v1/', include('product.api.v1.urls'))
]