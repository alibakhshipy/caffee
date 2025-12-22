from django.contrib import admin
from .models import Product, FooterLinkBox2, ProductAboutCaffe, ProductVisit, ProductVariant, ProductGr

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','is_featured', 'is_new', 'author']
    list_editable = ['is_featured', 'is_new']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "Footer_link_box":
            kwargs["queryset"] = FooterLinkBox2.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)

# Register کردن FooterLinkBox2 تا خودش هم تو admin دیده بشه
@admin.register(FooterLinkBox2)
class FooterLinkBox2Admin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'parent']  # مثلا title و slug

# Register بقیه مدل‌ها
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVisit)
admin.site.register(ProductVariant)
admin.site.register(ProductGr)
admin.site.register(ProductAboutCaffe)