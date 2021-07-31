from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

from .models import Song

class SongListView(ListView):
    queryset = Song.objects.all()


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
