from _ast import Store
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.

# def store(request):
#     products = Product.objects.all()
#     return render(request, 'store/store.html', {
#         'products': products
#     })


class StoreListView(ListView):
    template_name = 'store/store.html'
    model = Product
    context_object_name = 'products'
    # paginate_by = 1   جهت تعداد محصولاتی که در صفحه نمایش داده شود

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