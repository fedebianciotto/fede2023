from django.db import models
import datetime

class Publicacion (models.Model):
    titulo = models.CharField(max_length=100)
    descripcion= models.TextField()
    imagen=models.ImageField(upload_to='blog/imagenes')
    fecha= models.DateField(datetime.date.today)

