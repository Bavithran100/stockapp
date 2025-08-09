import os
from pathlib import Path
from dotenv import load_dotenv
from mongoengine import connect, disconnect


load_dotenv()

# -------------------------
# Base directory
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# Security settings
# -------------------------
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-please-change-this-key')

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'Stocktrackpro.herokuapp.com').split(',')

# -------------------------
# Application definition
# -------------------------
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


MONGODB_URI = os.environ.get(
    'MONGODB_URI',
    'mongodb+srv://Bavithran:bavi0914o@cluster0.ez3remi.mongodb.net/mydb?retryWrites=true&w=majority&appName=Cluster0'
)

# Disconnect any existing default connection before connecting
disconnect(alias='default')
connect(host=MONGODB_URI)

# -------------------------
# Static files (CSS, JavaScript, Images)
# -------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -------------------------
# Session settings
# -------------------------
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
