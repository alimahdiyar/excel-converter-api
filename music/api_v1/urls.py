from django.urls import path
from rest_framework.schemas import get_schema_view

from music.api_v1.views import (
    SongListView, SongDetailView, ProducerListView, ArtistListView, SearchFilterView
)

# schema_view = get_schema_view(
#     openapi.Info(
#         title="CafePay API",
#         default_version='development version',
#         description="CafePay API Documentation\n@spsina\n@SadafAsad",
#         contact=openapi.Contact(email="snparvizi75@gmail.com"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

app_name = 'Songs'
urlpatterns = [
    path('music/', SongListView.as_view(), name='Song-list'),
    path('music/<int:id>/', SongDetailView.as_view(), name='Song-detail'),
    path('producer/', ProducerListView.as_view(), name='Song-list'),
    path('artist/', ArtistListView.as_view(), name='Song-list'),
    path('search/', SearchFilterView.as_view(), name='Song-list'),

        # docs
    # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# urlpatterns += router.urls