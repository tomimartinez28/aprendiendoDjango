from django.shortcuts import render


# Create your views here.

# view que renderiza la pagina de inicio
def indexView(request):
    return render(request, 'index.html', {})


