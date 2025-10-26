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
    template_name = 'store/arobica.html'
    model = Product
    context_object_name = 'arobica'
    paginate_by = 8

class RobustaListView(ListView):
    template_name = 'store/robusta.html'
    model = Product
    context_object_name = 'robusta'    
    paginate_by = 8
    
class TorkListView(ListView):
    template_name = 'store/tork.html'
    model = Product
    context_object_name = 'tork'
    paginate_by = 8

class EquipmentListView(ListView):
    template_name = 'store/equipment.html'
    model = Product
    context_object_name = 'equipment'
    paginate_by = 8
    
class MakerListView(ListView):
    template_name = 'store/maker.html'
    model = Product
    context_object_name = 'maker'
    paginate_by = 8 

class AccessoriesListView(ListView):
    template_name = 'store/accessories.html'
    model = Product
    context_object_name = 'accessories'
    paginate_by = 8            