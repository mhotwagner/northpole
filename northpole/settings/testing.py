from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'northpole-docker-testing',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = []

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '..', 'static_source'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, '..' 'media')
MEDIA_URL = '/media/'

LOGGER_FILE_PATH = os.path.join(BASE_DIR, '..', 'test.log')
