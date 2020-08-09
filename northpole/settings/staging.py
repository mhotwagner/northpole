from .base import *
import django_heroku


django_heroku.settings(locals())

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '..', 'static_source'),
)

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, '..' 'media')
MEDIA_URL = '/media/'

# LOGGING['handlers']['file'] = {
#     'class': 'logging.FileHandler',
#     'filename': '/var/log/northpole-app.log',
# }
#
# LOGGING['loggers'] = {
#     'django': {
#         'handlers': ['file'],
#         'level': os.getenv('NORTHPOLE_LOG_LEVEL', 'DEBUG'),
#     },
#     'apps': {
#         'handlers': ['file'],
#         'level': os.getenv('NORTHPOLE_LOG_LEVEL', 'DEBUG'),
#     },
# }

# Channels!
ASGI_APPLICATION = 'northpole.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [
                (os.getenv('REDIS_URL', 'redis'), os.getenv('NORTHPOLE_REDIS_PORT', 6379)),
            ],
        },
    },
}
