from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    calle = models.CharField(max_length=100, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    colonia = models.CharField(max_length=100, blank=True, null=True)
    cp = models.IntegerField(blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    ocupacion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    genero = models.CharField(max_length=100, blank=True, null=True)
    email2 = models.EmailField(blank=True, null=True)
    background = models.ImageField(upload_to="backImages", blank="true", null="true")

    def __str__(self):
        return self.user
