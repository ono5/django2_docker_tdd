from .settings import *
import os

# Disable debug
DEBUG = True

# Set secret key
SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

# Must be explicitly specified when Debug is disabled
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'PORT': os.environ.get('DB_PORT', '5432')
    },
    # Remove the following option https://stackoverflow.com/questions/15839989/django-south-keyerror-engine
    # 'OPTIONS': {
    #   'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
    # }
}

# # Database settings
# DATABASES = {
#     'default': {
#         'ENGINE': 'mysql.connector.django',
#         'NAME': os.environ.get('MYSQL_DATABASE','todobackend'),
#         'USER': os.environ.get('MYSQL_USER','todo'),
#         'PASSWORD': os.environ.get('MYSQL_PASSWORD','password'),
#         'HOST': os.environ.get('MYSQL_HOST','localhost'),
#         'PORT': os.environ.get('MYSQL_PORT','3306'),
#     },
#     'OPTIONS': {
#       'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#     }
# }

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "example"
    }
}

STATIC_ROOT = os.environ.get('STATIC_ROOT', '/public/static')
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', '/public/media')