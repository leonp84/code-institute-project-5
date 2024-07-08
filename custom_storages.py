from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


# Settings needed by the django-storages library

# https://django-storages.readthedocs.io/en/1.9.1/backends/amazon-S3.html

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
