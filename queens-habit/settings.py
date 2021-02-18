"""
Django settings for queens-habit project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys
import dj_database_url

# .env config:
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Determine if we are on local or production
if os.getenv('ENV') == 'development':
  # If we are on development, use the `DB_NAME_DEV` value
  # from the .env file as the database name
  DB_NAME = os.getenv('DB_NAME_DEV')
  DB = {
      'ENGINE': 'django.db.backends.postgresql',
      'NAME': DB_NAME,
      'USER': 'postgres',
      'PASSWORD': 'Myboygeorge1969',
  }
  # Set debug to true
  DEBUG = True
  # Only allow locally running client at port 7165 for CORS
  CORS_ORIGIN_WHITELIST = ['http://localhost:7165']
else:
  # If we are on production, use the dj_database_url package
  # to locate the database based on Heroku setup
  DB = dj_database_url.config()
  # Set debug to false
  DEBUG = False
  # Only allow the `CLIENT_ORIGIN` for CORS
  CORS_ORIGIN_WHITELIST = [
    os.getenv('CLIENT_ORIGIN')
  ]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# Default database as defined above depending on development
# or production environment
DATABASES = {
    'default': DB
}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# This uses either a .env key or Heroku config var called SECRET
SECRET_KEY = os.getenv('SECRET')

# Application definition

INSTALLED_APPS = [
    # Our custom apps
    'api',
    # DRF
    'rest_framework',
    'rest_framework.authtoken',
    # Django built-in
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'queens-habit.urls'

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

WSGI_APPLICATION = 'queens-habit.wsgi.application'

# Django Rest Framework
#
# The default authentication class for all views will be TokenAuthentication
# which defines how we authenticate
# https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
#
# The default permission class for all views will be IsAuthenticated to require
# authentication for access
# https://www.django-rest-framework.org/api-guide/permissions/#isauthenticated
#
# These can be overridden on individual views
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# optional package: http://whitenoise.evans.io/en/stable/django.html
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Use the custom user model as the auth user for the admin view
AUTH_USER_MODEL = 'api.User'
