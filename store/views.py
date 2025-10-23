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

class ArobicaView(ListView):
    template_name = 'store/arobica.html'
    model = Product
    context_object_name = 'arobica'