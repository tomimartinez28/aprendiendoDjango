from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Usuario(AbstractUser):
    telefono = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255, blank=True, null=True)
    es_admin = models.BooleanField(default=False)



