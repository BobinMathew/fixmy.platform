"""
Django settings for fixmydjango project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import datetime
import django_heroku
import os

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l$1cu6s#k*+8(5ai05+y3-0w+xw^(+)@t=(2r704g_y+yub@d='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', False)

ALLOWED_HOSTS = [
    'localhost',
    '35.234.67.137',
]


# Application definition

INSTALLED_APPS = [
    'anymail',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'djoser',
    'fixmyapp.apps.FixmyappConfig',
    'markdownx',
    'rest_framework',
    'rest_framework_gis',
    'reversion',
]

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fixmydjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'fixmydjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('DATABASE_NAME', 'docker'),
        'USER': os.getenv('DATABASE_USER', 'docker'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'docker'),
        'HOST': 'db',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = os.getenv('STATIC_URL', '/static/')

STATIC_ROOT = '/code/static'


# Request body size
# https://docs.djangoproject.com/en/2.1/ref/settings/#data-upload-max-memory-size

DATA_UPLOAD_MAX_MEMORY_SIZE = 26214400


# CORS headers
# https://github.com/ottoyiu/django-cors-headers

CORS_ORIGIN_ALLOW_ALL = True


# Amazon S3
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')

AWS_QUERYSTRING_AUTH = os.getenv('AWS_QUERYSTRING_AUTH', False)

AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')

AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')

AWS_S3_USE_SSL = os.getenv('AWS_S3_USE_SSL', True)

AWS_S3_SIGNATURE_VERSION = os.getenv('AWS_S3_SIGNATURE_VERSION', 's3v4')


# Anymail
# https://anymail.readthedocs.io/en/stable/

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')

DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'info@fixmyberlin.de')

ANYMAIL = {
    'MAILJET_API_KEY': os.getenv('MAILJET_API_KEY', ''),
    'MAILJET_SECRET_KEY': os.getenv('MAILJET_SECRET_KEY', ''),
}

NEWSLETTER_LIST_ID = os.getenv('NEWSLETTER_LIST_ID')

# Mapbox
# https://www.mapbox.com/api-documentation/#uploads

MAPBOX_ACCESS_TOKEN = os.getenv('MAPBOX_ACCESS_TOKEN', '')

MAPBOX_UPLOAD_REGION = os.getenv('MAPBOX_UPLOAD_REGION', 'us-east-1')

MAPBOX_UPLOAD_NAME = {
    'main': os.getenv('MAPBOX_UPLOAD_NAME_MAIN', ''),
    'side': os.getenv('MAPBOX_UPLOAD_NAME_SIDE', '')
}

MAPBOX_UPLOAD_TILESET = {
    'main': os.getenv('MAPBOX_UPLOAD_TILESET_MAIN', ''),
    'side': os.getenv('MAPBOX_UPLOAD_TILESET_SIDE', ''),
}

MAPBOX_UPLOAD_URL = os.getenv('MAPBOX_UPLOAD_URL', 'https://api.mapbox.com/uploads/v1')

MAPBOX_USERNAME = os.getenv('MAPBOX_USERNAME', '')


# REST Framework
# http://dajngo-rest-framework.org

REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}


# REST framework JWT
# http://getblimp.github.io/django-rest-framework-jwt/#rest-framework-jwt-auth

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=180),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=720)
}


# Djoser
# https://djoser.readthedocs.io/en/stable/index.html

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': os.getenv('PASSWORD_RESET_CONFIRM_URL', ''),
    'PASSWORD_RESET_CONFIRM_FRONTEND_URL': os.getenv('PASSWORD_RESET_CONFIRM_FRONTEND_URL', '')
}


# Activate Django-Heroku
# https://devcenter.heroku.com/articles/django-app-configuration

django_heroku.settings(locals())
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'


# Feature-Toggles

TOGGLE_NEWSLETTER = bool(os.getenv('TOGGLE_NEWSLETTER', 0))
