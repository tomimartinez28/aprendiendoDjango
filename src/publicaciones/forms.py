from django import forms
from .models import Publicaciones


class CrearPublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['categoria', 'titulo', 'post']
        labels = {
            'titulo': '',
            'post' : '',
            'categoria' : ''
        }

        widgets = {
            'categoria' : forms.Select(attrs={'class' : 'form-select', 'placeholder' : 'Categoria'}),
            'titulo' : forms.TextInput(attrs= {'placeholder' : 'Aca va el titulo', 'class' : 'form-control'}),
            'post' : forms.TextInput(attrs= {'placeholder' : 'Escribi algo...', 'class' : 'form-control'} )
        }
    