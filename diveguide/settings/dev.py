from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cvn5+eq6lw4w#kkgg4-eu41n#)^c%r1vkmj&_3bs58#tgjz4^1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
