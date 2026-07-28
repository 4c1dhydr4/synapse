from synapse import settings
from django.core.files.storage import FileSystemStorage
from storages.backends.s3boto3 import S3Boto3Storage

class LocalStorage(FileSystemStorage):
	location = settings.MEDIA_ROOT

class MediaStorage(S3Boto3Storage):
	location = 'media'
	# default_acl = 'public-media'
	file_overwrite = False

class PrivateMediaStorage(S3Boto3Storage):
	location = 'private-media'
	default_acl = None
	file_overwrite = False

def select_private_storage():
	return LocalStorage() if settings.DEBUG else PrivateMediaStorage()

def select_public_storage():
	return LocalStorage() if settings.DEBUG else MediaStorage()