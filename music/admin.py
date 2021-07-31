from django.contrib import admin

from .models import Artist,Song

# Register your models here.
admin.site.register(Song)
admin.site.register(Artist)