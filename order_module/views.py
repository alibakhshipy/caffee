# products/views.py
from django.views.generic import DetailView
from product.models import Product, ProductVariant

class ProductDetailView(DetailView):
    model = Product
    template_name = "order_module/detail_order.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        context["variants"] = product.variants.all()  # همه ویریانت‌های محصول
        context["variantgr"] = product.variants.all()
        return context