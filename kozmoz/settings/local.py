# Local Django
from .base import *
from .local_secrets import (EMAIL_HOST_USER, EMAIL_HOST_PASSWORD,
    DEFAULT_FROM_EMAIL
    )

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/validators/

AUTH_PASSWORD_VALIDATORS = []


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Source Code

SOURCE_CODE_BACKEND = 'https://github.com/kaganndemirr/kozmoz-project-backend'


# Domain

DOMAIN_BACKEND = 'http://127.0.0.1:8000'


# Email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = 587
