# from django.shortcuts import render
# from django.shortcuts import redirect, get_object_or_404, render
# from product.models import ProductVariant, Product
# from .models import Order, OrderDetail
# from django.http import HttpRequest, HttpResponse, JsonResponse


# def add_to_cart(request):
#     product_id = request.GET.get("product_id")
#     variant_id = request.GET.get("variant_id")
#     count = int(request.GET.get("count", 1))

#     raw_price = request.GET.get("price", "0")
#     clean_price = raw_price.replace(",", "")
#     try:
#         price = int(clean_price)
#     except:
#         price = 0

#     if variant_id in [None, "", "null", "None", "undefined"]:
#         variant_id = None

#     if not request.user.is_authenticated:
#         return JsonResponse({
#             "status": "not_none",
#             "text": "لطفاً وارد شوید!",
#             "icon": "warning",
#             "confirmButtonText": "باشه"
#         })
        
#     product = Product.objects.filter(
#         id=product_id, 
#         is_active=True, 
#         is_delete=False,
#         is_available=True).first()
    
#     if not product:
#         return JsonResponse({
#             "status": "error",
#             "text": "این محصول در حال حاضر موجود نیست",
#             "icon": "error",
#             "confirmButtonText": "متوجه شدم"
#         })

#     variant = None
#     if variant_id:
#         variant = ProductVariant.objects.filter(
#             id=variant_id, 
#             product_id=product_id
#         ).first()
        
#         if variant and not variant.is_available:
#             return JsonResponse({
#                 "status": "error",
#                 "text": "این وزن از محصول موجود نیست",
#                 "icon": "error",
#                 "confirmButtonText": "متوجه شدم"
#             })

#     current_order, created = Order.objects.get_or_create(is_paid=False, user=request.user)

#     detail_order = current_order.orderdetail_set.filter(
#         product_id=product_id,
#         variant_id=variant_id
#     ).first()

#     if detail_order:
#         detail_order.count += count
#         detail_order.final_price = price
#         detail_order.save()
#     else:
#         OrderDetail.objects.create(
#             order=current_order,
#             product=product,
#             variant=variant,
#             count=count,
#             final_price=price
#         )

#     return JsonResponse({
#         "status": "success",
#         "text": "به سبد خرید اضافه شد",
#         "icon": "success",
#         "confirmButtonText": "باشه"
#     })

from django.shortcuts import render, redirect, get_object_or_404
from product.models import ProductVariant, Product
from .models import Order, OrderDetail
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
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

    # بررسی احراز هویت کاربر
    if not request.user.is_authenticated:
        return JsonResponse({
            "status": "not_auth",
            "text": "لطفاً ابتدا وارد حساب کاربری خود شوید!",
            "icon": "warning",
            "confirmButtonText": "ورود"
        })

    # پیدا کردن محصول و بررسی فعال بودن
    product = Product.objects.filter(
        id=product_id, 
        is_active=True, 
        is_delete=False
    ).first()
    
    if not product:
        return JsonResponse({
            "status": "error", 
            "text": "محصول مورد نظر یافت نشد", 
            "icon": "error",
            "confirmButtonText": "متوجه شدم"
        })
    
    # 🔴 بررسی موجودی محصول
    if not product.is_available:
        return JsonResponse({
            "status": "error",
            "text": "متأسفانه این محصول در حال حاضر موجود نیست!",
            "icon": "error",
            "confirmButtonText": "متوجه شدم"
        })

    # پیدا کردن واریانت (اگر وجود دارد)
    variant = None
    if variant_id:
        variant = ProductVariant.objects.filter(
            id=variant_id, 
            product_id=product_id
        ).first()
        
        # 🔴 بررسی موجودی واریانت (اگر واریانت دارد)
        if variant and hasattr(variant, 'is_available') and not variant.is_available:
            return JsonResponse({
                "status": "error",
                "text": "متأسفانه این وزن از محصول در حال حاضر موجود نیست!",
                "icon": "error",
                "confirmButtonText": "متوجه شدم"
            })

    # پیدا کردن یا ایجاد سفارش جاری
    current_order, created = Order.objects.get_or_create(
        is_paid=False, 
        user=request.user
    )

    # بررسی آیا این محصول قبلاً در سبد خرید وجود دارد
    detail_order = current_order.orderdetail_set.filter(
        product_id=product_id,
        variant_id=variant_id
    ).first()

    if detail_order:
        # 🔴 بررسی موجودی قبل از افزایش تعداد
        # اگر مجموع درخواست شده بیشتر از موجودی باشد
        requested_total = detail_order.count + count
        if product.stock_quantity and requested_total > product.stock_quantity:
            return JsonResponse({
                "status": "error",
                "text": f"موجودی محصول کافی نیست. فقط {product.stock_quantity} عدد موجود است.",
                "icon": "warning",
                "confirmButtonText": "متوجه شدم"
            })
        
        detail_order.count += count
        detail_order.final_price = price
        detail_order.save()
    else:
        # 🔴 بررسی موجودی برای اولین بار اضافه کردن
        if product.stock_quantity and count > product.stock_quantity:
            return JsonResponse({
                "status": "error",
                "text": f"موجودی محصول کافی نیست. فقط {product.stock_quantity} عدد موجود است.",
                "icon": "warning",
                "confirmButtonText": "متوجه شدم"
            })
        
        OrderDetail.objects.create(
            order=current_order,
            product=product,
            variant=variant,
            count=count,
            final_price=price
        )

    return JsonResponse({
        "status": "success",
        "text": "محصول با موفقیت به سبد خرید اضافه شد",
        "icon": "success",
        "confirmButtonText": "باشه"
    })