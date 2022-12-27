from django.db import models

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.CharField(max_length=50)
    usuario_modificacion = models.CharField(max_length=50)

    class Meta:
        abstract = True

