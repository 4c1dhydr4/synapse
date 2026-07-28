from synapse import settings
from django.core.files.storage import FileSystemStorage
from storages.backends.s3 import S3Storage

class LocalStorage(FileSystemStorage):
	location = settings.MEDIA_ROOT

class PrivateMediaStorage(S3Storage):
	default_acl = "private"
	querystring_auth = True
	querystring_expire = 3600
	file_overwrite = False
