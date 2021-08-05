from django.urls import path, include
from .views import (
    SongListView, SongDetailView,
)

from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('all_songs', SongViewSet)

app_name = 'Songs'
urlpatterns = [
    path('music/', SongListView.as_view(), name='Song-list'),
    path('music/<int:id>/', SongDetailView.as_view(), name='Song-detail'),
] 

# urlpatterns += router.urls