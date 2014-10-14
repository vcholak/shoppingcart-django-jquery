"""
Django settings for sportsite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SPORTS_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['itaurica.com']  # must be set when DEBUG = False


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authapp',
    'sports'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sportsite.urls'

WSGI_APPLICATION = 'sportsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sports',
        'USER': 'produsr',
        'PASSWORD': os.environ['SPORTS_DATABASE_PASSWORD'],
        'HOST': '',  # '' means localhost
        'PORT': '',  # '' means the default port
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Toronto'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# STATIC_URL = '/'  # "GET / HTTP/1.1" 404 1600
STATIC_URL = '/static/'

# localhost:8000/ - (404) Directory indexes are not allowed here.
# but localhost:8000/index.html - OK
STATICFILES_DIRS = (
    '../static/',
)


# Please note that STATIC_ROOT is the path where Django collects static files in, rather than the path that it serves files from.
# You should not maintain STATIC_ROOT yourself!
# While in production, you should collect all the static files in STATIC_ROOT, by running manage.py collectstatic.
# Then you can serve that folder directly through your webserver (e.g. nginx, Apache), rather than through Django.

# if STATIC_ROOT value is contained in STATICFILES_DIRS then error:
# django.core.exceptions.ImproperlyConfigured: The STATICFILES_DIRS setting should not contain the STATIC_ROOT setting
#STATIC_ROOT = "../static/"

# if MEDIA_URL == STATIC_URL then django.core.exceptions.ImproperlyConfigured: The MEDIA_URL and STATIC_URL settings must have different values
#MEDIA_URL = '/static/'