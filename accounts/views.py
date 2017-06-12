from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets
from .serializers import ProfileSerializer, UserSerializer
from .models import Profile
from django.contrib.auth.models import User


# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #permission_classes = (permissions.IsAuthenticated,)


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer