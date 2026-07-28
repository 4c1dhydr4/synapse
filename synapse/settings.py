from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

ADMINS = (
	('Luis Quiroz', 'quirozburga@gmail.com'),
)

# Application definition

DJANGO_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sitemaps',
	'django.contrib.sites',
)

THIRD_PARTY_APPS = (
	'channels',
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	'allauth.socialaccount.providers.google',
	'django_celery_results',
	'rest_framework',
	'rest_framework.authtoken',
	'webpush',
	'django_crontab',
)

LOCAL_APPS = (
	'apps.core',
	'apps.security',
)

INSTALLED_APPS = ('daphne',) + DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

DEBUG_MIDDLEWARE = [
	'querycount.middleware.QueryCountMiddleware',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django_permissions_policy.PermissionsPolicyMiddleware',
	'whitenoise.middleware.WhiteNoiseMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'allauth.account.middleware.AccountMiddleware',
]

if DEBUG:
	MIDDLEWARE = DEBUG_MIDDLEWARE + MIDDLEWARE

	QUERYCOUNT = {
		'THRESHOLDS': {
			'MEDIUM': 50,
			'HIGH': 200,
			'MIN_TIME_TO_LOG':0,
			'MIN_QUERY_COUNT_TO_LOG':0
		},
		'IGNORE_REQUEST_PATTERNS': [],
		'IGNORE_SQL_PATTERNS': [],
		'DISPLAY_DUPLICATES': None,
		'RESPONSE_HEADER': 'X-DjangoQueryCount-Count',
		'NOCOLOR': False,
	}

SITE_ID = 1

# Rest Framework
REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES': (
		'rest_framework.permissions.IsAuthenticated',
		'rest_framework.permissions.DjangoModelPermissions',
	),
	'DEFAULT_RENDERER_CLASSES': (
		'rest_framework.renderers.JSONRenderer',
	),
	'DEFAULT_PARSER_CLASSES': (
		'rest_framework.parsers.JSONParser',
	)
}

ROOT_URLCONF = 'synapse.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR/'templates'],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

# WSGI_APPLICATION = 'synapse.wsgi.application'

# Asyncho and Channels
ASGI_APPLICATION = "synapse.asgi.application"

CHANNEL_LAYERS = {
	'default': {
		'BACKEND': 'channels_redis.pubsub.RedisPubSubChannelLayer',
		'CONFIG': {
			"hosts": [config('REDIS_CHANNELS_HOST')],
		},
	},
}

# Databases
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': config('DB_NAME'),
		'USER': config('DB_USER'),
		'PASSWORD': config('DB_PASSWORD'),
		'HOST': config('DB_HOST'),
		'PORT': config('DB_PORT', cast=int),
		'TEST': {
			'NAME': 'test_synapse'
		}
	}
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cache
CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.redis.RedisCache',
		'LOCATION': config('REDIS_CACHE_LOCATION'),
		'TIMEOUT': 60 * 60 * 24,
	}
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# Authentication
AUTHENTICATION_BACKENDS = (
	'apps.security.accounts.SocialAuthBackend',
)

AUTH_USER_MODEL = "security.User"

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
	'google': {
		'SCOPE': [
			'profile',
			'email',
		],
		'AUTH_PARAMS': {
			'access_type': 'online',
		}
	}
}

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

if not DEBUG:
	ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Lima'
USE_I18N = False
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = ((BASE_DIR/'static'),)
STATIC_ROOT = BASE_DIR/'s3'

# Storage
STORAGES = {
	"default": {
		"BACKEND": 'synapse.storage.MediaStorage' ,
	},
	"staticfiles": {
		"BACKEND": 'whitenoise.storage.CompressedStaticFilesStorage',
	},
}

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/'media'

# File Paths
ERRORS_PATH = config('ERRORS_PATH')

#AWS
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)
AWS_S3_OBJECT_PARAMETERS = {
	'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'media'
AWS_DEFAULT_ACL = config('AWS_DEFAULT_ACL')

# Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_SUBJECT_PREFIX = config('EMAIL_SUBJECT_PREFIX')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_SSL = config('EMAIL_USE_SSL', cast=bool)
EMAIL_USE_LOCALTIME = config('EMAIL_USE_LOCALTIME', cast=bool)


# LOGIN_REDIRECT_URL = reverse_lazy('success_auth')

# Security

# Content Security Policy
CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", "https://fonts.googleapis.com", "https://use.fontawesome.com", "https://apis.google.com")
CSP_FONT_SRC = ("'self'", "https://fonts.gstatic.com","https://use.fontawesome.com", "https://apis.google.com")
CSP_IMG_SRC = ("'self'", "data:","https://synapse-v2.s3.amazonaws.com", "http://www.google-analytics.com/",
	"https://synapse.pe", "maps.gstatic.com", "*.googleapis.com", "*.youtube.com", "*.ytimg.com", "*.ggpht")
CSP_SCRIPT_SRC = ("'self'", "https://maps.googleapis.com", "https://apis.google.com")
CSP_SCRIPT_SRC_ELEM = ("'self'", "https://maps.googleapis.com", "https://apis.google.com", "https://maps.google.com", "http://www.google-analytics.com/ga.js",
	"https://www.googletagmanager.com",)
CSP_CONNECT_SRC = ("'self'","https://maps.googleapis.com", "https://www.google-analytics.com/")
CSP_FRAME_SRC = ("'self'", "https://accounts.google.com", "https://synapse-v2.s3.amazonaws.com/", "https://www.youtube.com/", "https://td.doubleclick.net/")
CSP_OBJECT_SRC = ("'self'",)
CSP_INCLUDE_NONCE_IN = ("script-src","font-src", "script-src-elem", 'frame-src')

# Permission Policy
PERMISSIONS_POLICY = {
	"accelerometer": ['self'],
	"autoplay": ['self'],
	"camera": ['self'],
	"display-capture": ['self'],
	"encrypted-media": ['self'],
	"fullscreen": ['self'],
	"geolocation": ['self'],
	"gyroscope": ['self'],
	"interest-cohort": ['self'],
	"magnetometer": ['self'],
	"microphone": ['self'],
	"midi": ['self'],
	"payment": ['self'],
	"usb": ['self'],
	"web-share": ['self'],
}

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 3600

if DEBUG:
	X_FRAME_OPTIONS = 'ALLOWALL'
	XS_SHARING_ALLOWED_METHODS = ['POST','GET','OPTIONS', 'PUT', 'DELETE']
else:
	SECURE_SSL_REDIRECT = False
	SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# CSRF Token
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', cast=lambda v: [s.strip() for s in v.split(',')])

# Celery
CELERY_TIMEZONE = 'America/Lima'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_RESULT_BACKEND = 'django-db'
CELERY_RESULT_EXTENDED = True
CELERY_CACHE_BACKEND = 'default'
CELERY_BROKER_URL = config('REDIS_CELERY_BROKER')

# TMS Version
from apps.core.system import (Git,)
SYNAPSE_VERSION = Git().get_tms_version()

if DEBUG:
	HOST = "http://localhost:8001"
else:
	HOST = config('APP_HOST')