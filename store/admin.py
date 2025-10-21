from django.contrib import admin
from . import models

# class ProductAdmin(admin.ModelAdmin):
    # list_filter = ['title', 'category', 'is_active']
    # # list_editable = ['title', 'price','is_active']
    # list_display = ['title', 'price', 'is_active', 'is_delete']
admin.site.register(models.Product)

