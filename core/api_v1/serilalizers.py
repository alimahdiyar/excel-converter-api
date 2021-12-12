from rest_framework import serializers

from core.models import ExcelPattern, ExcelPatternUploadedFile


class ExcelPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelPattern
        fields = ['pk', 'name', 'owner']


class ExcelPatternUploadedFileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelPatternUploadedFile
        fields = ['the_file']


class ExcelPatternUploadedFileSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = ExcelPatternUploadedFile
        fields = ['pk', 'pattern', 'file_url']

    def get_file_url(self, obj):
        if obj.the_file is None:
            return None
        return self.context['request'].build_absolute_uri(obj.the_file.url)
