[![Build Status](https://travis-ci.org/treilly94/diveguide.svg?branch=dev)](https://travis-ci.org/treilly94/diveguide)

# Diveguide

## Config
The project settings has been split into multiple files to separate out the different environments.
The settings file to use can be defined by either using the below flag with manage.py or setting the below environment
variable.
```--settings=diveguide.settings.< ENV >```

```DJANGO_SETTINGS_MODULE=diveguide.settings.< ENV >```

Some environment specific config (secrets) are set through environment variables.
These variables are listed below

### Django variables
* SECRET_KEY

### Database variables
* DATABASE_NAME
* DATABASE_USER
* DATABASE_PASSWORD
* DATABASE_HOST
* DATABASE_PORT

### API variables
* GOOGLE_MAPS_API