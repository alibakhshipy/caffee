from django.urls import path
from . import views

urlpatterns = [
    # shoping list
    path('', views.StoreListView.as_view(), name='store_caf'),
    path('arabica', views.ArabicaListView.as_view(), name='arabica'),
    path('robusta', views.RobustaListView.as_view(), name='robusta'),
    path('tork', views.TorkListView.as_view(), name='tork'),
    path('equipment', views.EquipmentListView.as_view(), name='equipment'),
    path('maker', views.MakerListView.as_view(), name='maker'),
    path('accessories', views.AccessoriesListView.as_view(), name='accessories'),
    
    # store equipments
    path('grinder', views.CaffeeGrinderListView.as_view(), name='grinder'),
    path('bank', views.CaffeeBankListView.as_view(), name='bank'),
    path('travel_mug', views.TravelMugListView.as_view(), name='travel_mug'),
    path('filter', views.FilterListView.as_view(), name='filter'),
    path('flask', views.FlaskListView.as_view(), name='flask'),
    path('shaker', views.ShakerListView.as_view(), name='shaker'),
]