from django.shortcuts import render

# from product.models import Product


# Create your views here.

def shop_cofe(request):
    return render(request, 'shop/shop_cafe.html')
