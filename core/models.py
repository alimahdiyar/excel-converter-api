from datetime import timedelta

from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


def file_upload_location(instance, filename):
    return "file/%d/generated-%s" % (instance.pattern.pk, filename)


class UserProfile(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile", blank=True,
                                       null=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class ExcelPattern(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name="patterns")


class ExcelPatternUploadedFile(models.Model):
    pattern = models.ForeignKey(ExcelPattern, on_delete=models.PROTECT, related_name="uploaded_files")
    the_file = models.FileField(upload_to=file_upload_location)
    # generated_file = models.FileField(blank=True, null=True, upload_to=file_upload_location)

    def __str__(self):
        return self.pattern.name + str(self.the_file)
