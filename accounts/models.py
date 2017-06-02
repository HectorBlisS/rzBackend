from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User)
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    colonia = models.CharField(max_length=100)
    cp = models.IntegerField()
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    ocupacion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.user
