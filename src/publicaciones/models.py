from django.db import models

# Create your models here.

# Esta clase crea una tabla para guardar las categorias
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre





# Clase crea una tabla para las publicaciones
class Publicaciones(models.Model):
    fecha = models.DateField(auto_now_add = True)
    titulo = models.CharField(max_length = 255)
    post = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, related_name='posteos', null= True)

    def __str__(self):
        return self.titulo