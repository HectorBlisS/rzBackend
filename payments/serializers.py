from rest_framework.serializers import ModelSerializer
from .models import Donacion
from projects.serializers import ProjectSerializer


class DonacionSerializer(ModelSerializer):
	proyecto = ProjectSerializer(many=False, read_only=True)
	class Meta:
		model = Donacion
		fields = "__all__"
