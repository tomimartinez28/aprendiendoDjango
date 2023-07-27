from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from .models import Contacto
from .forms import ContactoForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ContactanosView(LoginRequiredMixin,CreateView):
    model = Contacto
    template_name = 'contacto/contacto.html'
    form_class = ContactoForm

    def get_success_url(self):
        return reverse('contacto:mensaje-enviado')

    def form_valid(self, form):
        f = form.save(commit=False)
        f.autor_id = self.request.user.id
        return super().form_valid(f)
    

def mensaje_enviado(request):
    return render(request, 'contacto/mensaje-enviado.html', {})