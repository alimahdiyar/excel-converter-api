from django.urls import path
from .views import (
    SongDeleteView,
    SongDetailView,
    SongListView,
    SongUpdateView,
   

)

app_name = 'Songs'
urlpatterns = [
    path('', SongListView.as_view(), name='Song-list'),
    path('<int:id>/', SongDetailView.as_view(), name='Song-detail'),
    path('<int:id>/update/', SongUpdateView.as_view(), name='Song-update'),
    path('<int:id>/delete/', SongDeleteView.as_view(), name='Song-delete'),
]