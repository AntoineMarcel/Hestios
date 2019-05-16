from django.contrib import admin
from .models import Ticket

# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'auteur', 'date')
    fieldsets = (
    ('Problème', {
        'description': "Merci d'être le plus précis possible, screen et liens si possible.",
        'fields': ('titre', 'description')
    }),)
    def save_model(self, request, obj, form, change):
        obj.auteur = request.user
        obj.save()

admin.site.register(Ticket, TicketAdmin)
