# Check the production settings
.PHONY: check
check:
	python manage.py check --deploy

# Start a local development server
.PHONY: devserver
devserver:
	python manage.py runserver
