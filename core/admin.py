from django.contrib import admin

# Register your models here.
from core.models import UserProfile, ExcelPatternUploadedFile, ExcelPattern

admin.site.register(UserProfile)
admin.site.register(ExcelPattern)
admin.site.register(ExcelPatternUploadedFile)
