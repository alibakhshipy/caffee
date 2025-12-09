from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404, render
from product.models import ProductVariant, Product
from .models import Order, OrderDetail
from django.http import HttpRequest, HttpResponse, JsonResponse

# def add_to_cart(request: HttpRequest):
#     # raw_price = request.GET.get('price', '0')
#     # clean_price = raw_price.replace('', ',')
#     product_id = int(request.GET.get('product_id'))
#     variant_id = int(request.Get.get('variant_id'))
#     count = int(request.GET.get('count', 1))
#     price = request.GET.get('price', 0)
    
#     if count < 1:
#          return JsonResponse({
#                 'status': 'invlid_count',
#                 'text': 'مقدار وارد شده معتبر نمیباشد',
#                 'confirmButtonText': 'بیخیال',
#                 'icon': 'warning'
#             })   
#     if request.user.is_authenticated:
#         product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
#         if product is not None:
#             variant = None
#             if variant_id:
#                 variant = ProductVariant.objects.filter(id=variant_id, product_id=product_id).first()
#             current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
#             detail_order = current_order.orderdetail_set.filter(product_id=product_id, variant_id=variant_id).first()
#             if detail_order is not None:
#                 detail_order.count += count
#                 detail_order.save()
#             else:
#                 new_order = OrderDetail(order_id=current_order.id, product_id=product_id, count=count, variant=variant, price=price)
#                 new_order.save()
                    
#             return JsonResponse({
#                 'status': 'success',
#                 'text': 'محصول به سبد خرید اضافه شد',
#                 'confirmButtonText': 'اوکی',
#                 'icon': 'success'
#             })
#         else:
#             return JsonResponse({
#                 'status': 'not_found',
#                 'text': 'محصول مورد نظر یافت نشد!',
#                 'confirmButtonText': 'اوکی',
#                 'icon': 'error'
#             })
#     return JsonResponse({
#         'status': 'not_none',
#         'text': 'لطفا وارد حساب کابری خود شوید',
#         'confirmButtonText': 'صفحه ورود',
#         'icon': 'error'
#     })
    
def add_to_cart(request):
    product_id = request.GET.get("product_id")
    variant_id = request.GET.get("variant_id")
    count = int(request.GET.get("count", 1))

    raw_price = request.GET.get("price", "0")
    clean_price = raw_price.replace(",", "")
    try:
        price = int(clean_price)
    except:
        price = 0

    if variant_id in [None, "", "null", "None", "undefined"]:
        variant_id = None

    if not request.user.is_authenticated:
        return JsonResponse({
            "status": "not_none",
            "text": "لطفاً وارد شوید!",
            "icon": "warning",
            "confirmButtonText": "باشه"
        })

    product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
    if not product:
        return JsonResponse({"status": "not_found", "text": "محصول یافت نشد", "icon": "error"})

    variant = None
    if variant_id:
        variant = ProductVariant.objects.filter(id=variant_id, product_id=product_id).first()

    current_order, created = Order.objects.get_or_create(is_paid=False, user=request.user)

    detail_order = current_order.orderdetail_set.filter(
        product_id=product_id,
        variant_id=variant_id
    ).first()

    if detail_order:
        detail_order.count += count
        detail_order.final_price = price   # یا مدل دوم: count * price
        detail_order.save()
    else:
        OrderDetail.objects.create(
            order=current_order,
            product=product,
            variant=variant,
            count=count,
            final_price=price   # ← به جای price
        )

    return JsonResponse({
        "status": "success",
        "text": "به سبد خرید اضافه شد",
        "icon": "success",
        "confirmButtonText": "باشه"
    })