from django.contrib import admin

from .models import Artist, Song, Category

# Register your models here.
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Category)