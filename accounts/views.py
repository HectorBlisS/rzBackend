# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProfileSerializer, UserSerializer
from .models import Profile
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions



class isSelfOrAdmin(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_object_permission(self, request, view, obj):
    		if request.user.is_staff or obj.user == request.user:
    			return True



class GetMyProfile(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	def get(self, request):
		
		profile, created = Profile.objects.get_or_create(user=request.user)
		# serializer = ProfileSerializer(profile, many=False)
		# return Response(serializer.data)

		serializer = UserSerializer(request.user)
		return Response(serializer.data)

	def post(self, request):
		profile, created = Profile.objects.get_or_create(user=request.user)
		# serializer = ProfileSerializer(profile, many=False)
		# return Response(serializer.data)

		print(request.data['photoURL'])

		if request.data['photoURL']:
			profile.photoURL = request.data['photoURL']
			profile.save()

		if request.data['uid']:
			profile.uid = request.data['uid']
			profile.save()
		

		serializer = UserSerializer(request.user)
		return Response(serializer.data)



class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    permission_classes = [permissions.AllowAny,]

    def get_permissions(self):
    	# print('action',self.action)
    	# print('method',self.request.method)
    	# print('permiso', self.permission_classes)
    	# if self.request.method == 'PUT':
    	if self.action == 'update':
    		self.permission_classes = [isSelfOrAdmin,]
    	# else:
    	# 	self.permissions_classes = None
    	return super(ProfileViewSet, self).get_permissions()




class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer