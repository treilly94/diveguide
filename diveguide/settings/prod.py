from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret_setting('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret_setting('DATABASE_NAME'),
        'USER': get_secret_setting('DATABASE_USER'),
        'PASSWORD': get_secret_setting('DATABASE_PASSWORD'),
        'HOST': get_secret_setting('DATABASE_HOST'),
        'PORT': get_secret_setting('DATABASE_PORT'),
    }
}

STATIC_ROOT = 'static'
