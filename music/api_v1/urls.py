from django.conf.urls import url
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from music.api_v1.views import (
    SongListView, SongDetailView, ProducerListView, ArtistListView, SearchFilterView, CategoryListView
)

schema_view = get_schema_view(
    openapi.Info(
        title="Station 49 API",
        default_version='development version',
        description="Station 49 API Documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = 'Songs'
urlpatterns = [
    path('music/', SongListView.as_view(), name='song-list'),
    path('music/<int:id>/', SongDetailView.as_view(), name='song-detail'),
    path('producer/', ProducerListView.as_view(), name='producer-list'),
    path('artist/', ArtistListView.as_view(), name='artist-list'),
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('search/', SearchFilterView.as_view(), name='Song-list'),

        # docs
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# urlpatterns += router.urls