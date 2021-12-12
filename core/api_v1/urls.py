from django.conf.urls import url
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token

from core.api_v1.views import (
    ExcelPatternUploadedFileCreateView, ExcelPatternListView
)

schema_view = get_schema_view(
    openapi.Info(
        title="Excel Converter API",
        default_version='development version',
        description="Excel Converter API Documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = 'Songs'
urlpatterns = [
    path('user_profile/pattern/list/', ExcelPatternListView.as_view(), name='pattern-list'),
    path('user_profile/pattern/<int:pk>/upload-excel/', ExcelPatternUploadedFileCreateView.as_view(), name='pattern-list'),
    path('user_profile/api-token-auth/', obtain_auth_token, name='api-token-auth'),

    # docs
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# urlpatterns += router.urls