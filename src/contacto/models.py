from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Contacto(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    asunto = models.CharField(max_length=255)
    mensaje = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, related_name='contado', null=True)
    
    def __str__(self) -> str:
        return self.asunto