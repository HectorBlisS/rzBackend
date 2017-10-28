from rest_framework.serializers import ModelSerializer
from .models import Donacion


class DonacionSerializer(ModelSerializer):
	class Meta:
		model = Donacion
		fields = "__all__"
