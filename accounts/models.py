from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

<<<<<<< HEAD
    user = models.OneToOneField(User)
=======
    user = models.OneToOneField(User, blank=True, null=True)
    photoURL = models.URLField(blank=True, null=True)
>>>>>>> aa2ea786fa1c38652a08c1341aa34a84de8fe65e
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
<<<<<<< HEAD
    background = models.IntegerField(blank=True, null=True)
=======
    background = models.ImageField(upload_to="backImages", blank="true", null="true")
    canPublish = models.BooleanField(default=False)
>>>>>>> aa2ea786fa1c38652a08c1341aa34a84de8fe65e

    def __str__(self):
        return self.user.username
