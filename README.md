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
* `pip install django-registration`
* `pip install psycopg2`

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
```

### Create Database
* Run `psql` to get into the Postgres shell
* Run `CREATE DATABASE helphelp2_dev;` in there

### Migrate Database
* `python manage.py migrate auth`
* `python manage.py migrate`

### Start Server
* `python manage.py runserver`

### Setup first User
* Go to [localhost:8000/account/register](http://localhost:8000/account/register/) to create a new user
* Run `python manage.py shell` to get into the python shell and run the following commands in there
  * `from django.contrib.auth.models import User`
  * `me = User.objects.get(pk=1)`
  * `me.is_active = True`
  * `me.is_staff = True`
  * `me.is_superuser = True`
  * `me.save()`
