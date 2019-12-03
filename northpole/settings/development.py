from .base import *

# from dotenv import load_dotenv
# load_dotenv(verbose=True)

DEBUG = True

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'northpole-development',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
)

AUTH_PASSWORD_VALIDATORS = []

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static_source'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOCAL = True

LOGGING['loggers'].update({
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
)
