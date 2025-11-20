from django.db import models
from django import forms

# Create your models here.
class Cliente (models.Model):
    nombre = models.CharField()
    telefono = models.CharField()
    correo = models.EmailField()
    contrasena = models.CharField()