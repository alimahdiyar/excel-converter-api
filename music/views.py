from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serilalizers import SongSerializer
from .models import Song


class SongListView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    search_fields = ['artist', 'category']


class SongDetailView(RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer