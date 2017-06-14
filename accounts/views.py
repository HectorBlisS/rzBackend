# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProfileSerializer, UserSerializer
from .models import Profile
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions



class GetMyProfile(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	def get(self, request):
		
		profile, created = Profile.objects.get_or_create(user=request.user)
		serializer = ProfileSerializer(profile, many=False)
		return Response(serializer.data)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #permission_classes = (permissions.IsAuthenticated,)


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer