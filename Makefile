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

# Run the unit tests
.PHONY: test
test:
	python manage.py test --settings=diveguide.settings.$(ENV)

# Lint
.PHONY: lint
lint: lint_diveguide lint_divesites

.PHONY: lint_diveguide
lint_diveguide:
	pylint --load-plugins pylint_django diveguide

.PHONY: lint_divesites
lint_divesites:
	pylint --load-plugins pylint_django divesites