from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets
from .serializers import ProjectSerializer, RewardSerializer
from .models import Project, Reward
from rest_framework.generics import ListAPIView
from rest_framework.pagination import (PageNumberPagination, LimitOffsetPagination,)

class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(author=self.request.user)

class ProjectViewSet(OwnerMixin, viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    paginate_by = 10
    max_paginate_by = 11


class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer


    # permission_classes = (permissions.IsAuthenticated,)

class PaginatedListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = LimitOffsetPagination
