from django.http import HttpRequest
from django.shortcuts import render
from order_cart.models import Order, OrderDetail
from django.shortcuts import redirect, get_object_or_404

from product.models import ProductGr



def user_basket(request: HttpRequest):
    curentorder, create = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = 0
    for order_detail in curentorder.orderdetail_set.all():
        total_amount += order_detail.product.price.amount * order_detail.count
    
    context={
        'order': curentorder,
        'sum': total_amount,
    }
    return render(request, 'shop/shop_cafe.html', context)


def remove_from_cart(request, detail_id):
    detail = get_object_or_404(OrderDetail, id=detail_id, order__user=request.user, order__is_paid=False)
    detail.delete()
    return redirect('user_basket')