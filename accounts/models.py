from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):


    user = models.OneToOneField(User, blank=True, null=True)
    photoURL = models.URLField(blank=True, null=True)
    uid = models.CharField(blank=True, null=True, max_length=140)

    edad = models.IntegerField(blank=True, null=True)
    calle = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=140,blank=True, null=True)
    colonia = models.CharField(max_length=100, blank=True, null=True)
    cp = models.CharField(max_length=140,blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    ocupacion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=140,blank=True, null=True)
    genero = models.CharField(max_length=100, blank=True, null=True)
    email2 = models.EmailField(blank=True, null=True)

    background = models.IntegerField(blank=True, null=True)

    canPublish = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username
