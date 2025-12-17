from unicodedata import category
from django.views.generic import ListView
from product.models import Product, FooterLinkBox2


class CategoryListView(ListView):
    template_name = 'store/category.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Product.objects.filter(
            Footer_link_box__slug=slug,
            is_active=True,
            is_delete=False
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        
        # گرفتن دسته‌بندی جاری
        category = FooterLinkBox2.objects.filter(slug=slug).first()
        context['category'] = category
        
        if category:
            # گرفتن زیردسته‌های این دسته‌بندی
            context['children'] = category.children.all()
            
            # گرفتن محصولات مرتبط
            context['related_products'] = Product.objects.filter(
                Footer_link_box=category,
                is_active=True,
                is_delete=False
            )[:8]  # محدود کردن به 8 محصول
            
        return context
