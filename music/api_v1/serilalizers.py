from rest_framework import serializers
from music.models import Song, Artist, Category, Producer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name', 'icon', 'cover']


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['pk', 'name']

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ['pk', 'name']


class SongSerializer(serializers.ModelSerializer):
    producers = ProducerSerializer(many=True)
    artist = ArtistSerializer()
    category = CategorySerializer()

    class Meta:
        model = Song
        fields = ['producers', 'pk', 'datetime', 'name', 'artist', 'song_file', 'icon', 'cover', 'category']
