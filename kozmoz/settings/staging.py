# Local Django
from .base import *
from .secrets import EMAIL_HOST_USER, DEFAULT_FROM_EMAIL, EMAIL_HOST_PASSWORD


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['*']


ADMINS = (
    # ("Your Name", "your_email@example.com"),
)


INSTALLED_APPS += (

)


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/validators/

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kozmozdb',
        'USER': 'kozmoz',
        'PASSWORD': 'test',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Domain

# Source Code

SOURCE_CODE_BACKEND = 'https://github.com/kaganndemirr/kozmoz-project-backend'

# Email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True
