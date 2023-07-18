from django.contrib import admin
from .models import Publicaciones, Categoria, Comentario


# Register your models here.
admin.site.register(Publicaciones)
admin.site.register(Categoria)
admin.site.register(Comentario)