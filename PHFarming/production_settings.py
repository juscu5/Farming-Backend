# prod_settings.py

from .settings import *

# Set DEBUG to False
DEBUG = True

# Set your production database settings
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

# Set allowed hosts
# ALLOWED_HOSTS = ['your_domain.com']


# CORS
ALLOWED_HOSTS = [
    'localhost',
    'http://localhost:5173',
    '127.0.0.1',
    'http://127.0.0.1',
    'http://192.168.1.103',
    'http://192.168.1.103:80',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    'http://192.168.1.103',
    'http://192.168.1.103:80',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1',
    'http://192.168.1.103',
    'http://192.168.1.103:80',
]

CORS_ORIGIN_WHITELIST = (
    'http://localhost:5173',
    'http://127.0.0.1',
    'http://192.168.1.103',
    'http://192.168.1.103:80',
)

SESSION_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_NAME = 'None'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CORS_ALLOW_CREDENTIALS = True

SESSION_EXPIRE_AT_BROWSER_CLOSE =True
SESSION_COOKIE_AGE = 1800