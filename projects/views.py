from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets
from .serializers import ProjectSerializer, RewardSerializer, ObservationSerializer, UpdateSerializer, PostUpdateSerializer, FollowSerializer, CategorySerializer
from .models import Project, Reward, Observaciones, Updates, Follow, Category
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.pagination import (PageNumberPagination, LimitOffsetPagination,)
from django.contrib.auth.models import User

from rest_framework.decorators import detail_route, list_route

class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        # print(self.request.user.is_staff)
        if self.request.user.is_staff:
            return qs
        return qs.filter(author=self.request.user)

class ProjectViewSet(OwnerMixin, viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # lookup_field = 'slug'


class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer


    # permission_classes = (permissions.IsAuthenticated,)

class PaginatedListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        qs = super(PaginatedListView, self).get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(validated=True)


class DetailProjectView(RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    

    def get_queryset(self):
        qs = super(DetailProjectView, self).get_queryset()
        return qs.filter(validated=True)

class PreviewDetailProjectView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class UserProjects(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):

        user = User.objects.get(id=self.kwargs['pk'])
        print(user)
        qs = super(UserProjects, self).get_queryset()
        return qs.filter(author=user)
    
class ObservationsViewSet(viewsets.ModelViewSet):
    queryset = Observaciones.objects.all()
    serializer_class = ObservationSerializer

class UpdatesViewSet(viewsets.ModelViewSet):
    queryset = Updates.objects.all()
    serializer_class = PostUpdateSerializer


class UserUpdates(ListAPIView):
    queryset = Updates.objects.all()
    serializer_class = UpdateSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        user = self.request.user
        follow = Follow.objects.all().filter(user_from=user)
        projects = []
        for f in follow:
            print(f.project)
            projects.append(f.project)
        #project = Project.objects.all().filter(followers=follow)
        qs = super(UserUpdates, self).get_queryset()
        return qs.filter(project__in=projects)


from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view

@csrf_exempt
@api_view(['POST'])
def follow_project(request):
    project=Project.objects.get(id=request.data)
    user=User.objects.get(id=request.user.id)
    #project=Project.objects.get(id=1)
    #user=User.objects.all()[1]
    #Follow.objects.get_or_create(user_from=user,project=project)
    follow, created=Follow.objects.get_or_create(user_from=user,project=project)
    if created==False:
        Follow.objects.get(id=follow.id).delete()

    #return Response({"message": "Following project", "data": request.data, "user":request.user.id})
    return Response({'follow':request.data, 'created':created})




class FollowedProjects(ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    def get_queryset(self):
        user = self.request.user
        qs = super(FollowedProjects, self).get_queryset()
        return qs.filter(user_from=user)

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer








