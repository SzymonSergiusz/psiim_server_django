from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render

# Create your views here.
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .models import *
from .serializers import *

from rest_framework import permissions, viewsets

class MountainViewSet(viewsets.ModelViewSet):
    serializer_class = MountainsSerializer
    queryset = Mountains.objects.all()
    permission_classes = [permissions.IsAuthenticated]


# TODO
# https://docs.djangoproject.com/en/5.0/topics/auth/passwords/#module-django.contrib.auth.hashers

