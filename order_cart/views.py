from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404, render
from product.models import ProductVariant, Product
from .models import Order, OrderDetail
from django.http import HttpRequest, HttpResponse, JsonResponse

def add_to_cart(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count', 1))
    price = request.GET.get('price')
    
    if count < 1:
         return JsonResponse({
                'status': 'invlid_count',
                'text': 'مقدار وارد شده معتبر نمیباشد',
                'confirmButtonText': 'بیخیال',
                'icon': 'warning'
            })   
    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            detail_order = current_order.orderdetail_set.filter(product_id=product_id).first()
            if detail_order is not None:
                detail_order.count += count
                detail_order.save()
            else:
                new_order = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                new_order.save()
                    
            return JsonResponse({
                'status': 'success',
                'text': 'محصول به سبد خرید اضافه شد',
                'confirmButtonText': 'اوکی',
                'icon': 'success'
            })
        else:
            return JsonResponse({
                'status': 'not_found',
                'text': 'محصول مورد نظر یافت نشد!',
                'confirmButtonText': 'اوکی',
                'icon': 'error'
            })
    return JsonResponse({
        'status': 'not_none',
        'text': 'لطفا وارد حساب کابری خود شوید',
        'confirmButtonText': 'صفحه ورود',
        'icon': 'error'
    })
    
 