#-*- encoding: utf-8 -*-
import sys
sys.stdout.buffer.write(("|\t "+ chr(9986) +" PySnipt'd " + chr(9986)+" \t|").encode('utf8'))
# from django.core.files.base import ContentFile
from requests import request, ConnectionError
from .models import Profile
# from mailin import mails



def save_profile_picture(backend, user, response, is_new,  *args, **kwargs):
	if backend.name == 'facebook' and is_new:
		user_model=user
		user_profile=Profile()
		user_profile.user=user_model
		# url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
		ide=response['id']
		correo=response['email']
		print(ide)


		try:
			user_profile.ide=ide
			user_profile.save()

		except ConnectionError:
			pass
			print("Error de conexion")
	# Dando bienvenida
		try:
			datos={
			'usuario':user
			}
			mails.welcome_mail(datos,correo)
		except:
			print("error en envio")