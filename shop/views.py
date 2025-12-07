from django.http import HttpRequest
from django.shortcuts import render
from order_cart.models import Order
# from product.models import Product


# Create your views here.

def user_basket(request: HttpRequest):
    curentorder, create = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = 0
    for order_detail in curentorder.orderdetail_set.all():
        total_amount += order_detail.product.price * order_detail.count
    
    context={
        'order': curentorder,
        'sum': total_amount
    }
    return render(request, 'shop/shop_cafe.html', context)
