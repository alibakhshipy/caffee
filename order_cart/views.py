from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404, render
from product.models import ProductVariant
from .cart import Cart

def add_to_cart(request):
    """
    افزودن یک واریانت به سبد خرید
    """
    if request.method == "POST":
        variant_id = request.POST.get("variant_id")
        quantity = int(request.POST.get("quantity", 1))
        variant = get_object_or_404(ProductVariant, id=variant_id)

        cart = Cart(request)  # ایجاد instance از کلاس Cart
        cart.add(variant, quantity)  # اضافه کردن آیتم

    return redirect("cart_detail")  # بعد از افزودن، نمایش صفحه سبد خرید


def remove_from_cart(request):
    """
    حذف یک آیتم از سبد خرید
    """
    if request.method == "POST":
        variant_id = request.POST.get("variant_id")
        variant = get_object_or_404(ProductVariant, id=variant_id)

        cart = Cart(request)
        cart.remove(variant)

    return redirect("cart_detail")


def update_cart(request):
    """
    تغییر تعداد یک آیتم
    """
    if request.method == "POST":
        variant_id = request.POST.get("variant_id")
        quantity = int(request.POST.get("quantity", 1))
        variant = get_object_or_404(ProductVariant, id=variant_id)

        cart = Cart(request)
        cart.update(variant, quantity)

    return redirect("cart_detail")


def cart_detail(request):
    """
    نمایش محتویات سبد خرید
    """
    cart = Cart(request)
    items = cart.items()
    total = cart.total()
    return render(request, "cart/cart_detail.html", {"items": items, "total": total})