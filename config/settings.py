from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
load_dotenv()
SECRET_KEY = os.environ.get('SECRET_KEY')


DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    # 'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    'crispy_forms',
    'allauth', # new
    'allauth.account', # new
    'debug_toolbar',

    #custom apps
    'accounts',
    'pages',
    'books',

]

ACCOUNT_USERNAME_REQUIRED = False 
ACCOUNT_AUTHENTICATION_METHOD = 'email' 
ACCOUNT_EMAIL_REQUIRED = True 
ACCOUNT_UNIQUE_EMAIL = True 



CRISPY_TEMPLATE_PACK = 'bootstrap4'


SITE_ID = 1

AUTHENTICATION_BACKENDS = (
'django.contrib.auth.backends.ModelBackend',
'allauth.account.auth_backends.AuthenticationBackend', # new
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_SESSION_REMEMBER = True

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "allauth.account.middleware.AccountMiddleware",
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 604800
CACHE_MIDDLEWARE_KEY_PREFIX = ''



LOGIN_REDIRECT_URL='/'
LOGOUT_REDIRECT_URL='/'
LOGIN_URL='account_login'

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'postgres',
'USER': 'postgres',
'PASSWORD': 'postgres',
'HOST': 'db',
'PORT': 5432
}}

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

#region TIME & LANGUAGE
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
#endregion

#region STATIC FILES & MEDIA
STATIC_URL = 'static/'
STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))

STATICFILES_FINDERS = [
"django.contrib.staticfiles.finders.FileSystemFinder",
"django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


MEDIA_URL = '/media/' 
MEDIA_ROOT = str(BASE_DIR.joinpath('media')) 
#endregion


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.CustomUser'

DEFAULT_FROM_EMAIL = 'admin@djangobookstore.com'

# ACCOUNT_EMAIL_VERIFICATION="mandatory"

import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]