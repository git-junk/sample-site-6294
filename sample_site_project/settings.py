from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!t97nj@_5r4io+f3l&(o9-!f=bmes$7y%#n^$4q4ezx952czjj'


# from socket import gethostname
# hostname = gethostname()

# if "DESKTOP-IMRHOOI" in hostname:
#     # デバッグ環境
#     DEBUG = True 
#     DATABASES = {
#         'default':{
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': 'sample_site_db',
#             'USER': 'postgres',
#             'PASSWORD': 'possql0701',
#             'HOST': '127.0.0.1',
#             'PORT': '5432',
#             }
#         }
#     ALLOWED_HOSTS = ['*'] 
# else:
#     # 本番環境
#     DEBUG = False
#     import dj_database_url
#     db_from_env = dj_database_url.config()
#     DATABASES = {
#         'default': dj_database_url.config()
#     }
#     ALLOWED_HOSTS = ['*']
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = ['sample-site-6294.herokuapp.com', '127.0.0.1', 'localhost']
# ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sample_site_app.apps.SampleSiteAppConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #追加
]

ROOT_URLCONF = 'sample_site_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'sample_site_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sample_site_db',
        'USER': 'postgres',
        'PASSWORD': 'possql0701',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
ALLOWED_HOSTS = ['*']

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEBUG = False
# if not DEBUG:
#     SECRET_KEY = os.environ['SECRET_KEY']
#     import django_heroku #追加
#     django_heroku.settings(locals()) #追加

#追加
# try:
#     from .local_settings import *
# except ImportError:
#     pass
