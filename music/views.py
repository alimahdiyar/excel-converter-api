from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .serilalizers import SongSerializer
from django.views.generic import (
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)

from .models import Song

class SongListView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetailView(DetailView):
    queryset = Song.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Song, id=id_)


class SongUpdateView(UpdateView):

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Song, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class SongDeleteView(DeleteView):
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Song, id=id_)

    def get_success_url(self):
        return reverse('Songs:Song-list')

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('song_name')
    serializer_class = SongSerializer
