from django.urls import path, include
from .views import (
    SongDeleteView,
    SongDetailView,
    SongListView,
    SongUpdateView,
    # SongViewSet,
)

from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('all_songs', SongViewSet)

app_name = 'Songs'
urlpatterns = [
    path('', SongListView.as_view(), name='Song-list'),
    path('<int:id>/', SongDetailView.as_view(), name='Song-detail'),
    path('<int:id>/update/', SongUpdateView.as_view(), name='Song-update'),
    path('<int:id>/delete/', SongDeleteView.as_view(), name='Song-delete'),
    # path('', include('router.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] 

# urlpatterns += router.urls