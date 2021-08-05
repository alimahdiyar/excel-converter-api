from rest_framework import serializers
from .models import Song, Artist, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'title', 'icon', 'cover']


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['pk', 'name']


class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    category = CategorySerializer()

    class Meta:
        model = Song
        fields = ['pk', 'song_name', 'artist', 'song_file', 'icon', 'cover', 'category']
