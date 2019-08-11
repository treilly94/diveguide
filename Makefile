ENV?=dev

# Check the settings
.PHONY: check
check:
	python manage.py check --deploy --settings=diveguide.settings.$(ENV)

# Start a local server
.PHONY: server
server:
	python manage.py runserver --settings=diveguide.settings.$(ENV)

# Create the tables in the database
.PHONY: migrate
migrate:
	python manage.py migrate --settings=diveguide.settings.$(ENV)
