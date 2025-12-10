from django.http import HttpRequest
from django.shortcuts import render
from order_cart.models import Order, OrderDetail
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
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




@login_required
@require_POST
def update_cart_item(request):
    detail_id = request.POST.get('detail_id')
    new_count = request.POST.get('count')
    
    try:
        detail = OrderDetail.objects.get(
            id=detail_id,
            order__user=request.user,
            order__is_paid=False
        )
        detail.count = int(new_count)
        detail.save()
        
        # محاسبه قیمت جدید
        total_price = detail.get_total_price()
        
        return JsonResponse({
            'status': 'success',
            'new_total_price': total_price,
            'new_count': detail.count
        })
    except OrderDetail.DoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)