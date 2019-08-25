release: python manage.py makemigrations --settings=diveguide.settings.dev
release: python manage.py migrate --settings=diveguide.settings.dev
web: gunicorn diveguide.wsgi