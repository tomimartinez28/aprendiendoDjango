from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from publicaciones.models import Publicaciones
from django.views.generic import ListView

# Create your views here.


'''
# view basada en funcion que renderiza la pagina de publicaciones 
def publicacionesView(request):
    ctx = {
        'posteos' : Publicaciones.objects.all().order_by('fecha')
    }
    return render(request, 'publicaciones.html', ctx)
'''

# View basada en clase que renderiza las publicaciones
class VerPublicaciones(ListView):
    model = Publicaciones
    template_name = 'publicaciones.html'
    context_object_name = 'posteos'


    def get_queryset(self):
        consulta_anterior = super().get_queryset()
        return consulta_anterior.order_by('fecha')
    