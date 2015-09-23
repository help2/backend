## Development Setup

### Pre-requirements
* Make sure you have Python (>= 2.7) installed
* Make sure you have pip installed+

* Make sure you have Postgres installed
* Make sure you have postgis installed
* Make sure you have gdal installed
* Make sure you have libgeoip installed

### Python dependencies
* `pip install django`
* `pip install django-simple-history`
* `pip install django-registration-redux`
* `pip install psycopg2`
* `pip install bootstrap-admin`

### Local config
Add a `heart/settings_local.py` file containing something like:

```python
# -*- coding: utf-8 -*-

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'helphelp2_dev',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost'
   }
}

SECRET_KEY = 'my super secret key'

ALLOWED_HOSTS = ["localhost"]

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

DEBUG = True

# you might overwrite the path of the log file here to avoid permission issues
```

### Create Database
* Run `psql` to get into the Postgres shell
* Run `CREATE DATABASE helphelp2_dev;` in there

### Migrate Database
* `python manage.py migrate auth`
* `python manage.py migrate`

### Setup first User
Run `python manage.py createsuperuser` and follow the instructions

### Start Server
`python manage.py runserver`
