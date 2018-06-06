"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
root = environ.Path(__file__) - 3
env = environ.Env(DEBUG=(bool, True), )
environ.Env.read_env(env_file=root('.env'))


ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
)
DEBUG = env('DEBUG', default=True)
INTERNAL_IPS = env.list('INTERNAL_IPS', [], default='127.0.0.1')
SECRET_KEY = env('SECRET_KEY')
SITE_ID = env('SITE_ID', default=1)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    'haystack',
    'registration',

    'mysite',
    'blog',
    'articles',
    'comments',
    'products',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [root('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': env.db(
        default='postgres://postgres:postgres@db:5432/postgres'
    )
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
    'mysite.authenticator.LoginAsUserBackend'
)

STATIC_URL = '/static/'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',  # noqa
        'URL': 'http://elasticsearch:9200/',
        'INDEX_NAME': 'haystack',
    },
}

CELERY_BROKER_URL = 'amqp://rabbitmq:5672/'

REGISTRATION_DEFAULT_FROM_EMAIL = 'admin@email.com'
SEND_ACTIVATION_EMAIL = True
SITE_ID = 2
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = False

LOGIN_REDIRECT_URL = 'home'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
ADMIN_HASH_SECRET = 'kjlgfjh'
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

CART_SESSION_ID = 'cart'
