from django.contrib import admin

from .models import Artist, Song, Category, Producer

# Register your models here.
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Category)
admin.site.register(Producer)