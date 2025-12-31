import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
from datetime import timedelta
load_dotenv()  # Load .env variables

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-test-key')

DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1', 't']

ALLOWED_HOSTS =["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'knox',
    'warranty_api',
     'home',
    
]
CSRF_TRUSTED_ORIGINS = [
    "https://server8.eport.ws",
    "http://server8.eport.ws",
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'warranty_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'warranty_core.wsgi.application'

# Database configuration for Supavisor (IPv4 + SSL)
DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASES = {
    'default': dj_database_url.parse(
        DATABASE_URL or "postgresql://postgres:Tafara9610.@aws-1-eu-west-1.pooler.supabase.com:5432/postgres?sslmode=require",
        conn_max_age=600
    )
}
DATABASES['default']['OPTIONS'] = {'sslmode': 'require'}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework
REST_FRAMEWORK = {
     "DEFAULT_AUTHENTICATION_CLASSES": (
        "warranty_api.authentication.tokenAuthentication",
        "knox.auth.TokenAuthentication",
    ),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
}
REST_KNOX = {
    "TOKEN_TTL": timedelta(weeks=6),   # Token lasts 6 weeks
    "AUTO_REFRESH": False,             # Optional: keep False unless you want sliding sessions
}

# CORS
CORS_ALLOWED_ORIGINS = ['http://localhost:3000', 'http://localhost:8000']

SERVICE_JWT_SECRET = os.environ.get('SERVICE_JWT_SECRET')
SERVICE_JWT_ISSUER = os.environ.get('SERVICE_JWT_ISSUER', 'nextjs-service')
SERVICE_JWT_AUDIENCE = os.environ.get('SERVICE_JWT_AUDIENCE', 'django-warranty-api')