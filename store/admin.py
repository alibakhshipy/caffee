from django.contrib import admin
from . import models
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_filter = ['title', 'category', 'is_active']
    list_display = ['title', 'price', 'is_active', 'is_delete']
    readonly_fields = ('slug')
    
admin.site.register(models.Product)
admin.site.register(models.FooterLinkBox3)
