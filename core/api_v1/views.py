from django_filters.rest_framework import DjangoFilterBackend
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.api_v1.serilalizers import ExcelPatternSerializer, ExcelPatternUploadedFileSerializer, \
    ExcelPatternUploadedFileCreateSerializer
from core.models import ExcelPattern, ExcelPatternUploadedFile


class ExcelPatternListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ExcelPattern.objects.all()
    serializer_class = ExcelPatternSerializer

    def get_queryset(self):
        user_profile = self.request.user.user_profile
        return ExcelPattern.objects.filter(owner=user_profile)


class ExcelPatternUploadedFileCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ExcelPatternUploadedFile.objects.all()
    serializer_class = ExcelPatternUploadedFileCreateSerializer
    parser_classes = (FormParser, MultiPartParser, FileUploadParser)

    def create(self, request, *args, **kwargs):
        user_profile = self.request.user.user_profile
        the_pattern = get_object_or_404(ExcelPattern.objects.all(), owner=user_profile, pk=kwargs['pk'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(pattern=the_pattern)
        return Response(ExcelPatternUploadedFileSerializer(instance, context=self.get_serializer_context()).data, status=201)
