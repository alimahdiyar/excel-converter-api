from django.db import models
from django.urls import reverse
# from django.db.models.fields import CharField

class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

# Create your models here.
class Song(models.Model):   
    id = models.AutoField(primary_key=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=300)
    song_file = models.FileField(upload_to= 'songs')

    def get_absolute_url(self):
        return reverse("")

    def __str__(self):
        return self.song_name + ' - ' + str(self.artist)