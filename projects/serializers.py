from rest_framework import serializers
from .models import Project, Reward

class RewardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reward
		fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
	rewards = RewardSerializer(many=True, read_only=True)
	class Meta:
		model = Project
		fields = '__all__'