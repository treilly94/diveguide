# Check the production settings
.PHONY: check
check:
	python manage.py check --deploy --settings=diveguide.settings.prod

# Start a local development server
.PHONY: rundev
rundev:
	python manage.py runserver --settings=diveguide.settings.dev
