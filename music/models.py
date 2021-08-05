from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

def song_icon_upload_location(instance, filename):
    return "artists/%d/song/%s/icon_%s" % (instance.artist.full_name, instance.song_name, filename)

def song_cover_upload_location(instance, filename):
    return "artists/%d/song/%s/cover_%s" % (instance.artist.full_name, instance.song_name, filename)

class Artist(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile", blank=True,
                                       null=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.full_name


# Create your models here.
class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=300)
    song_file = models.FileField(upload_to='songs')
    icon = models.ImageField(upload_to=song_icon_upload_location,
                             null=True,
                             blank=True)
    cover = models.ImageField(upload_to=song_cover_upload_location,
                             null=True,
                             blank=True)

    def __str__(self):
        return self.song_name + ' - ' + str(self.artist)
