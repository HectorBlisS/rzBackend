from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

<<<<<<< HEAD
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'id', 'email']
=======
>>>>>>> aa2ea786fa1c38652a08c1341aa34a84de8fe65e

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
