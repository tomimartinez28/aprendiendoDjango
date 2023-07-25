from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Usuario(AbstractUser):
    telefono = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255, blank=True, null=True)
    es_colaborador = models.BooleanField(default=False)
    imagen_perfil = models.ImageField(upload_to='imagenes_perfil', null=True, blank=True)


