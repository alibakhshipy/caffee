from django.contrib import admin
from django.http import HttpRequest

from . import models
from .models import Product, FooterLinkBox2

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','is_featured', 'is_new', 'author']

    def save_model(self, request:HttpRequest, obj:Product, form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)



admin.site.register(models.FooterLinkBox2)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductVisit)
