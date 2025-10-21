from django.contrib import admin
from .models import Site_setting, FooterLink, FooterLinkBox

class Site_settingAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

admin.site.register(Site_setting)
admin.site.register(FooterLinkBox)
admin.site.register(FooterLink, Site_settingAdmin)