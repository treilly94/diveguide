.EXPORT_ALL_VARIABLES:

ENV?=local

# Lint
.PHONY: lint
lint: lint_diveguide lint_divesites

.PHONY: lint_diveguide
lint_diveguide:
	pylint --load-plugins pylint_django diveguide

.PHONY: lint_divesites
lint_divesites:
	pylint --load-plugins pylint_django divesites

# Check the settings
.PHONY: check
check:
	python manage.py check --deploy --settings=diveguide.settings.$(ENV)

# Create new migrations based on the changes to the models
.PHONY: makemigrations
makemigrations:
	python manage.py makemigrations --settings=diveguide.settings.$(ENV)

# Create the tables in the database
.PHONY: migrate
migrate: makemigrations
	python manage.py migrate --settings=diveguide.settings.$(ENV)

# Start a local server
.PHONY: server
server: migrate
	python manage.py runserver --settings=diveguide.settings.$(ENV)

# Run the unit tests
.PHONY: test
test:
	python manage.py test --settings=diveguide.settings.$(ENV)

# Generate the static files
.PHONY: collectstatic
collectstatic:
	python manage.py collectstatic --noinput --settings=diveguide.settings.$(ENV)
