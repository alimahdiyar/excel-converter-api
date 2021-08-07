from django_filters.rest_framework import DjangoFilterBackend
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Song, Artist, Producer, Category
from .serilalizers import SongSerializer, ArtistSerializer, ProducerSerializer, CategorySerializer


class ArtistListView(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ProducerListView(ListAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class SongListView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['artist', 'category', 'producers']
    order_by = '-datetime'


class SongDetailView(RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SearchFilterView(ObjectMultipleModelAPIView):
    querylist = [
        {
            'queryset': Artist.objects.all(),
            'serializer_class': ArtistSerializer,
            'label': 'artist',
        },
        {
            'queryset': Category.objects.all(),
            'serializer_class': CategorySerializer,
            'label': 'category'
        },
        {
            'queryset': Producer.objects.all(),
            'serializer_class': ProducerSerializer,
            'label': 'producer'
        },
        {
            'queryset': Song.objects.all(),
            'serializer_class': SongSerializer,
            'label': 'song'
        },
    ]
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
