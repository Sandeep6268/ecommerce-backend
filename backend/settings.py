from pathlib import Path
from datetime import timedelta
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-bpx_3t9hx9zsdr@pyjom77p$69lk3hff_0g4wkz2$qo&&=hnlc'

DEBUG = True

ALLOWED_HOSTS = ['*']  # For Render and localhost access


# -------------------
# INSTALLED APPS
# -------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',

    'products',
    'cart',
    'users',
    'djoser',
]

# -------------------
# MIDDLEWARE
# -------------------
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',  # must be before CommonMiddleware
    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------
# CORS + CSRF
# -------------------
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "https://ecommerce-frontend-fv2p.onrender.com",
    "http://localhost:3000",
    "http://localhost:5173",
]

CSRF_TRUSTED_ORIGINS = [
    "https://ecommerce-frontend-fv2p.onrender.com",
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://ecommerce-backend-da9u.onrender.com",
]

# SESSION_COOKIE_SAMESITE = 'Lax'
# CSRF_COOKIE_SAMESITE = 'Lax'
# CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_HTTPONLY = True

# Optional: If hosting frontend on subdomain
SESSION_COOKIE_DOMAIN = ".onrender.com"
CSRF_COOKIE_DOMAIN = ".onrender.com"

# -------------------
# REST FRAMEWORK & JWT
# -------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'SERIALIZERS': {
        'user_create': 'users.serializers.UserCreateSerializer',  # Optional: use your custom serializer
        'user': 'users.serializers.UserSerializer',
        'current_user': 'users.serializers.UserSerializer',
    },
}


# -------------------
# SESSION SETTINGS
# -------------------
SESSION_COOKIE_AGE = 3600  # 1 hour
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SAVE_EVERY_REQUEST = True

# -------------------
# URL & WSGI
# -------------------
ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# -------------------
# DATABASE
# -------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'zub_db',
        'USER': 'zub_db_user',
        'PASSWORD': 'RgP6QL6oXeMWwmkFoPZxb7DITzIidu0c',
        'HOST': 'dpg-d1h1ofmmcj7s73dbg5g0-a.oregon-postgres.render.com',
        'PORT': '5432',
    }
}

# -------------------
# AUTH
# -------------------
AUTH_USER_MODEL = 'users.User'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------
# EMAIL SETTINGS
# -------------------
FRONTEND_URL = 'https://sandeep6268.github.io/ecommerce-frontend'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sandybanna1137@gmail.com'
EMAIL_HOST_PASSWORD = 'yseu jyrs kutw ysuj'
DEFAULT_FROM_EMAIL = 'sandybanna1137@gmail.com'

# -------------------
# INTERNATIONALIZATION
# -------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------
# STATIC & MEDIA
# -------------------
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

if os.environ.get('RENDER'):
    DEBUG = False
    ALLOWED_HOSTS += ['ecommerce-backend-da9u.onrender.com']

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)

    os.environ['DJANGO_COLLECTSTATIC'] = '1'

# -------------------
# AUTO FIELD
# -------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
