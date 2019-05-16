from django.contrib import admin
from .models import Villes
from django.utils.html import format_html
from django.utils import timezone
from django.urls import path
from .views import my_view

class VillesAdmin(admin.ModelAdmin):
   list_display   = ('ville','cp', 'lien_recherche')
   search_fields  = ('ville', 'cp')
   def lien_recherche(self, obj):
      return format_html("<a href='/admin/verificateur/{url}'>{url}</a>", url=obj.ville)

admin.site.register(Villes, VillesAdmin)

admin.site.site_header = "Administration d'Hestios"
admin.site.site_title = "Hestios Admin"
admin.site.index_title = "Panel d'administration Hestios"

def get_admin_urls(urls):
    def get_urls():
        my_urls = [
            path('verificateur/<str:endroit>', admin.site.admin_view(my_view))
        ]
        return my_urls + urls
    return get_urls

admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls