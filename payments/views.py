from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from projects.models import Reward, Project
import conekta
conekta.api_key = "key_sqCLgHarDSoaR2PWKsTZoA"
conekta.api_version = "2.0.0"


class ExecutePay(APIView):
	permission_classes = (permissions.IsAuthenticated,)

	def post(self, request):

		#sacamos los datos del diccionario
		data = request.data
		print(data)
		rewardId = data['rewardId']
		if rewardId:
		# si si llega reward, sacas los datos y montos
			reward = get_object_or_404(Reward, pk=rewardId)
			print(reward)
		else:
		# si no  llega reward, cobras libre *****
			print('llego falso', rewardId)
			amount = data['amount']
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
		try:
			order = conekta.Order.create({
		      "line_items": [{
		          "name": "Tacos",
		          "unit_price": 1000,
		          "quantity": 12
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
		    "metadata": { "description": "Compra de creditos: 300(MXN)", "reference": "1334523452345" },
		    "charges":[{
		      "payment_method": {
		        "type": "default"
		      }
		    }]
		  })
		except conekta.ConektaError as e:
			order = {"payment_status":"Falló"}
			print(order)
			print (e)

		# cobramos

		# exito: guardamos el input en base de datos y el id del cliente en profile
		# error: respondemos con la respuesta de conekta

		# respondemos 
		return Response(order['payment_status'])
