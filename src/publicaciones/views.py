from django.shortcuts import render
from publicaciones.models import Publicaciones

# Create your views here.

# view que renderiza la pagina de publicaciones
def publicacionesView(request):
    ctx = {
        'posteos' : Publicaciones.objects.all()
    }
    return render(request, 'publicaciones.html', ctx)
