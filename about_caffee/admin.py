from django.contrib import admin

from about_caffee import models

# Register your models here.
admin.site.register(models.BlogPost)
admin.site.register(models.BlogCategory)