from rest_framework.serializers import ModelSerializer
from .models import Donacion
from projects.serializers import ProjectSerializer, RewardSerializer
from accounts.serializers import UserSerializer


class DonacionSerializer(ModelSerializer):
	donador = UserSerializer(many=False, read_only=True)
	proyecto = ProjectSerializer(many=False, read_only=True)
	recompensa = RewardSerializer(many=False,read_only=True)

	class Meta:
		model = Donacion
		fields = "__all__"

