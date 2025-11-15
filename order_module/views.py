from django.shortcuts import render
from django.views.generic import DetailView
from product.models import Product
# Create your views here.

class ProductDetailView(DetailView):
    template_name = 'order_module/detail_order.html'
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'slug'