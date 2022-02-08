from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100 , verbose_name="Nombre")
    imagen = models.ImageField(upload_to = 'imagenes/', verbose_name="Imagen" , null = True)
    descripcion = models.TextField(null=True , verbose_name="Descripcion")

    def __str__(self):
        return self.nombre

    def delete(self , using=None , keep_parents = False ):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()