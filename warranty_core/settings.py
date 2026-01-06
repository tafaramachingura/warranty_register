import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
from datetime import timedelta

# Load base .env
load_dotenv()  # Load `.env`

# Load environment-specific variables from `.env.<ENV>` where ENV is one of:
# DJANGO_ENV, ENV, ENVIRONMENT. If not provided and DEBUG=True, try `.env.dev`.
_env_name = os.environ.get('DJANGO_ENV') or os.environ.get('ENV') or os.environ.get('ENVIRONMENT')
if _env_name:
    load_dotenv(f".env.{_env_name}", override=True)
else:
    if os.environ.get('DEBUG', 'False').lower() in ['true', '1', 't']:
        load_dotenv('.env.dev', override=True)


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-test-key')

DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1', 't']

ALLOWED_HOSTS = os.environ.get(
    'ALLOWED_HOSTS',
    'localhost,127.0.0.1'
).split(',')

FORCE_SCRIPT_NAME = "/register"

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


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
    "https://vm2.eport.ws",
    "http://vm2.eport.ws",
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
        DATABASE_URL ,
        conn_max_age=600
    )
}
DB_SSL = os.environ.get('DB_SSL', 'true').lower() in ('true', '1', 't')
if DB_SSL:
    DATABASES['default'].setdefault('OPTIONS', {})['sslmode'] = 'require'

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
CORS_ALLOWED_ORIGINS = os.environ.get('CONS_ALLOWED_ORIGINS', '').split(',')

SERVICE_JWT_SECRET = os.environ.get('SERVICE_JWT_SECRET')
SERVICE_JWT_ISSUER = os.environ.get('SERVICE_JWT_ISSUER', 'nextjs-service')
SERVICE_JWT_AUDIENCE = os.environ.get('SERVICE_JWT_AUDIENCE', 'django-warranty-api')