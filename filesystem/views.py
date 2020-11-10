# from django.shortcuts import render


from rest_framework import viewsets
from rest_framework.permissions import \
    IsAuthenticatedOrReadOnly

from filesystem.models import File, Hash
from filesystem.serializers import FileSerializer, HashSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


class HashViewSet(viewsets.ModelViewSet):
    queryset = Hash.objects.all()
    serializer_class = HashSerializer
