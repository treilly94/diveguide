"""
Django settings for a development server on heroku.

Extends base.py
"""

# pylint: disable=W0401,W0614

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': os.environ['DATABASE_PORT'],
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Simplified static file serving used with heroku.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Simplified static file serving Used with heroku.
# https://warehouse.python.org/project/whitenoise/
MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')
