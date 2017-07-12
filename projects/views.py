from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets
from .serializers import ProjectSerializer, RewardSerializer, ObservationSerializer, UpdateSerializer
from .models import Project, Reward, Observaciones, Updates, Follow
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.pagination import (PageNumberPagination, LimitOffsetPagination,)
from django.contrib.auth.models import User

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
    serializer_class = UpdateSerializer

class UserUpdates(ListAPIView):
    queryset = Updates.objects.all()
    serializer_class = UpdateSerializer

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









