from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'id', 'email', 'is_staff']

class ProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	class Meta:
		model = Profile
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	profile = ProfileSerializer(read_only=True)
	class Meta:
		model = User
		fields = '__all__'
