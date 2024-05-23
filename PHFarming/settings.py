"""
Django settings for PHFarming project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ipquuxmr-4--ga2+i^0f%j&y_n-yd%mj8_=^pf_0$3el4xwsjc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #

AUTHENTICATION_BACKENDS = [
    'User.credentialsChecker.CustomUserBackend',
]


AUTH_USER_MODEL = 'User.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    "rest_framework",
    "Dashboard",
    "Tracker",
    "RFP",
    "SubmitForm",
    "User",
    "workload",
    "corsheaders",
    "costsavings",
]

    # 

# ALLOWED_HOSTS = ['*']
# CORS_ALLOW_ALL_ORIGINS = True

# CORS
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'http://localhost:5173',
    'http://127.0.0.1:5173',
]
 
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5173',
    'http://localhost:5173'
]
 
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:5173',
    'http://localhost:5173'
]
 
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:5173',
    'http://localhost:5173'
)

SESSION_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_NAME = 'None'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CORS_ALLOW_CREDENTIALS = True

SESSION_EXPIRE_AT_BROWSER_CLOSE =True
SESSION_COOKIE_AGE = 1800

# SECURE_HSTS_SECONDS = 1800  #
# SECURE_SSL_REDIRECT = True  #
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True #
# SECURE_HSTS_PRELOAD = True #

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PHFarming.urls'

path = "Tracker/"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(path, 'templates')],
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

WSGI_APPLICATION = 'PHFarming.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'HOST': 'JUNELPC\\SQLEXPRESS',
        'NAME': 's4',
        'USER': '',
        'PASSWORD': '',
        'OPTIONS' : {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
        # 'ATOMIC_REQUESTS': True #if true it will allow all VIEWS to become atomic transaction
    },
    
    'ccms_db' : {
        'ENGINE': 'mssql',
        'HOST':'JUNELPC\\SQLEXPRESS',
        'NAME': 'CCMS',
        'USER':'',
        'PASSWORD':'',
        'PORT': '',
        'OPTIONS':{
            'driver':'ODBC Driver 17 for SQL Server',
            # 'isolation_level':'READ UNCOMMITTED' #to prevent deadlocks
        }
    },
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'standard': {
#             'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard',
#         },
#         'file': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': BASE_DIR/'logs'/'logfile.log',
#             'maxBytes': 1024 * 1024 * 5,  # 5 MB
#             'backupCount': 5,
#             'formatter': 'standard',
#         },
#     },
#     'loggers': {
#         '': {
#             'handlers': ['console', 'file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'django': {
#             'handlers': ['console', 'file'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#         'your_app': {
#             'handlers': ['console', 'file'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#         # Add more loggers for your apps as needed
#     },
# }

# Load local settings
# try:
#     from .local_settings import *
# except ImportError:
#     pass

# # Load production settings if applicable
# if 'PRODUCTION' in os.environ:
#     from .production_settings import *