from rest_framework import serializers
from .models import Project, Reward, Category, Observaciones, Updates, Follow
from accounts.serializers import UserSerializer



class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class RewardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reward
		fields = '__all__'

class ObservationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Observaciones
		fields = '__all__'

class ProjectTwoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = [ 'id']

# class FollowSerializer(serializers.ModelSerializer):
# 	user=UserSerializer(many=True, read_only=True)
# 	project=ProjectSer(many=True, read_only=True)
# 	class Meta:
# 		model = Follow
# 		fields = '__all__'


class UpdateSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Updates
		fields = '__all__'
		depth=1

class PostUpdateSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Updates
		fields = '__all__'
		
		

class ProjectSerializer(serializers.ModelSerializer):
	rewards = RewardSerializer(many=True, read_only=True)
	observation = ObservationSerializer(many=True, read_only=True)
	#followers = FollowSerializer(many=True, read_only=True)
	updates = UpdateSerializer(many=True, read_only=True)
	category = CategorySerializer(read_only=True, many=True)
	author = UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
	class Meta:
		model = Project
		fields = '__all__'
		lookup_field = 'slug'

	def create(self, validated_data):
		c = Category.objects.all().filter(slug='salud')
		p = Project.objects.create(**validated_data)
		p.category = c
		p.save()

		return p

class FollowSerializer(serializers.ModelSerializer):
	project = ProjectSerializer(read_only=True)
	class Meta:
		model = Follow
		fields = '__all__'
