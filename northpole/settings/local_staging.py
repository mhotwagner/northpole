from .base import *

from dotenv import load_dotenv
load_dotenv(dotenv_path='northpole/.staging.env', verbose=True)


ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB', 'northpole-staging'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '..', 'static_source'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, '..' 'media')
MEDIA_URL = '/media/'
