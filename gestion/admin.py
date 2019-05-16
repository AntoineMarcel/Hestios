from django.contrib import admin
from .models import Fiche,Commentaire, Facturation
from django.utils.text import Truncator
from django.utils.html import format_html
from django.utils import timezone

class FacturationInLine(admin.TabularInline):
   model = Facturation
   readonly_fields = ('date', 'facture')
   classes = ['collapse']
   extra = 0

class CommentairesInLine(admin.TabularInline):
   model = Commentaire
   readonly_fields = ('date',)
   classes = ['collapse']
   extra = 0

class CommentaireAdmin(admin.ModelAdmin):
   list_display   = ('fiche','fiche_prenom', 'date','apercu_com')
   list_filter    = ('fiche',)
   search_fields  = ('fiche__nom',)
   fields = ('commentaires', 'fiche')

   def fiche_prenom(self, Fiche):
      return Fiche.fiche.prenom
   def apercu_com(self, Commentaire):
      return Truncator(Commentaire.commentaires).chars(40, truncate='...')

   fiche_prenom.short_description = 'Prenom'
   apercu_com.short_description = 'Aperçu du commentaire'

class FicheAdmin(admin.ModelAdmin):
   def nom_colored(self, obj):
      color = 'red'
      now = timezone.now()
      if (obj.paiement != None and (now.year == obj.paiement.year and now.month == obj.paiement.month)):
         color = 'green'
      return format_html('<b style="color:{};">{}</b>', color, obj.nom)

   nom_colored.short_description = 'nom'
   list_display   = ('nom_colored', 'prenom', 'age', 'cp', 'date', 'paiement' )
   list_filter    = ('paiement',)
   search_fields  = ('nom', 'adresse')
   inlines = [CommentairesInLine, FacturationInLine]
   inline_type = 'tabular'  # or could be 'stacked'

   fieldsets = (
    # Fieldset 1 : info sur la personne
   ('Identité', {
      #   'classes': ['wide',],
        'fields': ('nom', 'prenom', 'age', 'genre')
    }),
    # Fieldset 2 : info contact et localisation
    ('Contact', {
       'description': 'Respecter la procedure afin de garder toutes les fiches selon le même prototypage.',
       'fields': ('adresse', 'ville', 'cp','telephone','mail', 'paiement')
    }),
)

admin.site.register(Fiche, FicheAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Facturation)