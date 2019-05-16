from datetime import datetime
from django.shortcuts import render
from gestion.models import Fiche
from django.db.models import Count, Q, Avg, Max, Min, Sum

def date_actuelle(request):
    dataset = Fiche.objects \
        .values('age') \
        .annotate(nombre=Count('age')) \
        .order_by('age')
    moyenne = Fiche.objects.all().aggregate(Avg('age'))
    moyenne = int(moyenne['age__avg'])
    return render(request, 'statistique/date.html', locals())