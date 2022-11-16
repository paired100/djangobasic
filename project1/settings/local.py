from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'empleados',

        'USER': 'postgres',

        'PASSWORD': '970106100',

        'HOST': 'localhost',

        'PORT': '5432',

    }
}


STATIC_URL = 'static/'
