from .base import *

SECRET_KEY = '1234567890'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': STATIC_MEDIA_DIR / 'db.sqlite3',
    }
}
