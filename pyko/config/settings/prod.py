from .base import *

ALLOWED_HOSTS = ['*']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []

DEBUG = False

DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'HOST': '13.125.16.6',
        'PORT': '5432',
        'NAME': 'pyko',
        'USER': 'admin',
        'PASSWORD': '1234'
    }
}