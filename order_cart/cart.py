class Cart:
    """
    این کلاس مدیریت سبد خرید session-based است.
    همه عملیات افزودن، حذف، آپدیت و محاسبه جمع کل در این کلاس انجام می‌شود.
    """

    SESSION_KEY = "cart"  # کلید session که اطلاعات سبد خرید داخلش ذخیره می‌شود

    def init(self, request):
        """
        هنگام ایجاد Cart، session و سبد خرید را می‌گیریم
        """
        self.session = request.session  # گرفتن session از request
        self.cart = self.session.get(self.SESSION_KEY, {})  # اگر سبد خرید موجود نبود، یک دیکشنری خالی بساز

    def add(self, variant, quantity=1):
        """
        افزودن یک واریانت به سبد خرید
        اگر قبلا وجود داشت، مقدار quantity جمع می‌شود
        """
        key = str(variant.id)  # کلید cart همیشه رشته باشد
        if key in self.cart:
            self.cart[key]["quantity"] += quantity
        else:
            self.cart[key] = {
                "product_id": variant.product.id,
                "title": variant.product.title,
                "variant_title": variant.title,
                "price": variant.price,
                "quantity": quantity,
            }
        self.save()  # همیشه بعد از تغییر، session را ذخیره کن

    def remove(self, variant):
        """
        حذف یک واریانت از سبد خرید
        """
        key = str(variant.id)
        if key in self.cart:
            del self.cart[key]
            self.save()

    def update(self, variant, quantity):
        """
        تغییر تعداد یک واریانت در سبد خرید
        اگر quantity <= 0 شود، آیتم حذف می‌شود
        """
        key = str(variant.id)
        if key in self.cart:
            if quantity <= 0:
                del self.cart[key]
            else:
                self.cart[key]["quantity"] = quantity
            self.save()

    def save(self):
        """
        ذخیره‌سازی سبد خرید در session
        """
        self.session[self.SESSION_KEY] = self.cart
        self.session.modified = True  # علامت‌گذاری session برای ذخیره شدن

    def clear(self):
        """
        پاک کردن کل سبد خرید
        """
        self.session[self.SESSION_KEY] = {}
        self.session.modified = True

    def items(self):
        """
        تمام آیتم‌های سبد خرید را برمی‌گرداند
        """
        return self.cart.values()

    def total(self):
        """
        جمع کل سبد خرید
        """
        return sum(item["price"] * item["quantity"] for item in self.cart.values())