from rest_framework import serializers
from .models import Project, Reward, Category
from accounts.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class RewardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reward
		fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
	rewards = RewardSerializer(many=True, read_only=True)
	category = CategorySerializer(read_only=True, many=True)
	author = UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
	class Meta:
		model = Project
		fields = '__all__'