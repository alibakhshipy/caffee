from django.urls import path
from . import views

urlpatterns = [
    path('', views.StoreListView.as_view(), name='store_caf'),
    path('arabica', views.ArabicaListView.as_view(), name='arabica'),
    path('robusta', views.RobustaListView.as_view(), name='robusta'),
    path('tork', views.TorkListView.as_view(), name='tork'),
    path('equipment', views.EquipmentListView.as_view(), name='equipment'),
    path('maker', views.MakerListView.as_view(), name='maker'),
    path('accessories', views.AccessoriesListView.as_view(), name='accessories'),
]