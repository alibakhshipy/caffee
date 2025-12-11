from _ast import Store
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class StoreListView(ListView):
    template_name = 'store/store.html'
    model = Product
    context_object_name = 'products'
    
# menu shoping
class ArabicaListView(ListView):
    template_name = 'store/arabica.html'
    model = Product
    context_object_name = 'arabica'
    paginate_by = 8

    def get_queryset(self):
        return Product.objects.filter(
            FooterLinkBox3__slug='Arabica',
            is_active=True,
            is_delete=True,
        )
class RobustaListView(ListView):
    template_name = 'store/robusta.html'
    model = Product
    context_object_name = 'robusta'    
    paginate_by = 8
    
    def get_queryset(self):
        return Product.objects.filter(
            FooterLinkBox3__slug = 'Robusta',
            is_active = True,
            is_delete = True
        ) 
    
class TorkListView(ListView):
    template_name = 'store/tork.html'
    model = Product
    context_object_name = 'tork'
    paginate_by = 8
    
    def get_queryset(self):
        return Product.objects.filter(
            FooterLinkBox3__slug = 'Tork',
            is_active = True,
            is_delete = True
        )

class EquipmentListView(ListView):
    template_name = 'store/equipment.html'
    model = Product
    context_object_name = 'equipment'
    paginate_by = 8
    
    def get_queryset(self):
        return Product.objects.filter(
            FooterLinkBox3__slug = 'Equipment',
            is_active = True,
            is_delete = True
        )
    
class MakerListView(ListView):
    template_name = 'store/maker.html'
    model = Product
    context_object_name = 'maker'
    paginate_by = 8 
    
    def get_queryset(self):
        return Product.objects.filter(
            FooterLinkBox3__slug = 'Maker',
            is_active = True,
            is_delete = True
        )

class AccessoriesListView(ListView):
    template_name = 'store/accessories.html'
    model = Product
    context_object_name = 'accessories'
    paginate_by = 8  
    
    def get_queryset(self):
        return Product.objects.filter(
            FooterLinkBox3__slug = 'Accessories',
            is_active = True,
            is_delete = True
        )          

# menu Equipments

class CaffeeGrinderListView(ListView):
    template_name = 'store/equipment/caffee-grinder.html'
    model = Product
    context_object_name = 'grinder'
    paginate_by = 8
    
    
    def get_queryset(self):
        return Product.objects.filter(
            FooterLinkBox3__slug = 'Grinder',
            is_active = True,
            is_delete = True
        )
        
class CaffeeBankListView(ListView):
    template_name = 'store/equipment/caffee-bank.html'
    model = Product
    context_object_name = 'bank'
    paginate_by = 8
    
    
    def get_queryset(self):
        return Product.objects.filter(
            FooterLinkBox3__slug = 'Bank',
            is_active = True,
            is_delete = True
        )        

class TravelMugListView(ListView):
    template_name = 'store/equipment/travel-mug.html'
    model = Product
    context_object_name = 'travel_mug'
    paginate_by = 8
    
    def get_queryset(self):
        return Product.objects.filter(
            FooterLinkBox3__slug = 'Travel_mug' 
        )

class FilterListView(ListView):
    template_name = 'store/equipment/filter.html'
    model = Product
    context_object_name = 'filter'
    paginate_by = 8
    
    def get_queryset(self):
        return Product.objects.filter(
            FooterLinkBox3__slug = 'Filter' 
        )

class FlaskListView(ListView):
    template_name = 'store/equipment/flask.html'
    model = Product
    context_object_name = 'flask'
    paginate_by = 8
    
    def get_queryset(self):
        return Product.objects.filter(
            FooterLinkBox3__slug = 'Flask' 
        )    
                

class ShakerListView(ListView):
    template_name = 'store/equipment/shaker.html'
    model = Product
    context_object_name = 'shaker'
    paginate_by = 8
    
    def get_queryset(self):
        return Product.objects.filter(
            FooterLinkBox3__slug = 'Shaker' 
        )          