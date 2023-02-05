from django.db import models

# Tablas para crear tareas (esta tabla va a estar usando el orm de django)
# Esta tabla tambien la podemos utilizar para guardar datos

class tareas(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True) # con blank=True le decimos que es un texto opcional