from .base import *


ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST', '0.0.0.0'),
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '..', 'static_source'),
)

STATIC_URL = 'http://storage.googleapis.com/northpole-staging/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, '..' 'media')
MEDIA_URL = '/media/'

LOGGING['handlers']['file'] = {
    'class': 'logging.FileHandler',
    'filename': '/var/log/northpole-app.log',
}

LOGGING['loggers'] = {
    'django': {
        'handlers': ['file'],
        'level': os.getenv('NORTHPOLE_LOG_LEVEL', 'DEBUG'),
    },
    'apps': {
        'handlers': ['file'],
        'level': os.getenv('NORTHPOLE_LOG_LEVEL', 'DEBUG'),
    },
}
