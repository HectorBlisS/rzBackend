from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from projects.models import Reward, Project
from rest_framework.viewsets import ModelViewSet

from .models import Donacion
from .serializers import DonacionSerializer

import conekta
conekta.api_key = "key_sqCLgHarDSoaR2PWKsTZoA"
conekta.api_version = "2.0.0"
conekta.locale = 'es'

class OwnerMixin(object):
	def get_queryset(self):
		proyectoId = self.request.GET.get("proyectoId")
		print("entero? ", proyectoId)
		#print("mixin: ", bool(propias) )
		qs = super(OwnerMixin, self).get_queryset()
# print(self.request.user.is_staff)
		if self.request.user.is_staff and proyectoId:
			proyecto = get_object_or_404(Project, id=proyectoId)
			return qs.filter(proyecto=proyecto)
		elif self.request.user.is_staff:
			return qs
		elif proyectoId:
			# print("toy aqui:", proyectoId)
			proyecto = get_object_or_404(Project, id=proyectoId, author=self.request.user)
			return qs.filter(proyecto=proyecto)
		return qs.filter(donador=self.request.user)

class DonacionViewSet(OwnerMixin, ModelViewSet):
	queryset = Donacion.objects.all()
	serializer_class = DonacionSerializer
	permission_classes = (permissions.IsAuthenticated,)


class ExecutePay(APIView):
	permission_classes = (permissions.IsAuthenticated,)

	def post(self, request):

		#sacamos los datos del diccionario
		data = request.data
		amount = 0
		print(data)
		rewardId = data['rewardId']
		if rewardId:
		# si si llega reward, sacas los datos y montos
			reward = get_object_or_404(Reward, pk=rewardId)
			amount = int(reward.amount) * 100
			print(reward)
			project = reward.project
		else:
		# si no  llega reward, cobras libre *****
			print('llego falso', rewardId)
			amount = int(data['amount']) * 100
		# reconocemos al usuario
		user = request.user

		# si id en profile buscamos al cliente en conekta
		if user.profile.conekta:
			try:
				customer = conekta.Customer.find(user.profile.conekta)
			except:
				pass
		else:
		# si no, lo creamos
			try:
				customer = conekta.Customer.create({
				    'name': data['name'],
				    'email': user.email,
				    'phone': data['tel'],
				    'payment_sources': [{
				      'type': 'card',
				      'token_id': data['token']['id']
				    }]
				  })
				user.profile.conekta = customer.id
				user.profile.save()
			except conekta.ConektaError as e:
				print (e)
		

		# creamos la orden y llenamos datos
		donacion = Donacion.objects.create(donador=user,proyecto=project, recompensa=reward, monto=amount/100)
		try:
			order = conekta.Order.create({
		      "line_items": [{
		          "name": reward.title,
		          "unit_price": amount,
		          "quantity": 1
		      }],
		      # "shipping_lines": [{
		      #     "amount": 1500,
		      #     "carrier": "mi compañia"
		      # }],
		      "currency": "MXN",
		      "customer_info": {
		       "customer_id": customer.id
		      },
		     #  "shipping_contact":{
		     #   "phone": "+52181818181",
		     #   "receiver": "Bruce Wayne",
		     #   "address": {
		     #     "street1": "Calle 123 int 2 Col. Chida",
		     #     "city": "Cuahutemoc",
		     #     "state": "Ciudad de Mexico",
		     #     "country": "MX",
		     #     "postal_code": "06100",
		     #     "residential": True
		     #   }
		     # },
		    "metadata": { 
		    	"description": reward.description, 
		    	"reference": reward.id 
		    	},
		    "charges":[{
		      "payment_method": {
		        "type": "default"
		      }
		    }]
		  })
			
			donacion.pagado = True
		except conekta.ConektaError as e:
			order = {"payment_status":"Falló"}
			print(order)
			print (e)

		# cobramos
		# ya lo cobra la orden:

		# exito: guardamos el input en base de datos y el id del cliente en profile
		# error: respondemos con la respuesta de conekta

		#guardamos donacion
		# creamos el objeto Donacion
		donacion.conekta = order.charges[0].id
		#print("code?",order.charges[0].id)
			# fin creamos donacion
		donacion.save()

		# respondemos 

		return Response(order['payment_status'])
