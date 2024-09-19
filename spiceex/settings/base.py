from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js', 'serviceworker.js')

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-lte0!a2d+-x311cfm(0437&91w%b4#-sjdq7#75c=_==hltgk)')

DEBUG = False  # False by default, can override in dev settings

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split()

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pwa',
    'store',
    'product',
    'siteinfo',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'spiceex.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.context_processors.categories_and_products_context',
                'siteinfo.context_processors.site_info_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'spiceex.wsgi.application'

# Default database configuration, overridden by dev or prod settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'spiceex_db',
        'USER': 'postgres',
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

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

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


PWA_APP_NAME = 'Spice-EX'
PWA_APP_SHORT_NAME = 'SpiceEX'  # Adding the short name
PWA_APP_DESCRIPTION = "Shop the best spices online at Spice-EX."
PWA_APP_THEME_COLOR = '#d2691e'  # Matching the theme color from the JSON
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'portrait-primary'  # Using 'portrait-primary' orientation from the JSON
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'

# Icons from the JSON
PWA_APP_ICONS = [
    {
        'src': 'static/images/logo-192.png',
        'sizes': '192x192',  # Matching size from the JSON
        'type': 'image/png'
    },
    {
        'src': 'static/images/logo-512.png',
        'sizes': '512x512',  # Matching size from the JSON
        'type': 'image/png'
    }
]

# Apple-specific icons, using the same as the general icons
PWA_APP_ICONS_APPLE = [
    {
        'src': 'static/images/logo-192.png',
        'sizes': '192x192',
        'type': 'image/png'
    }
]

# Adding splash screens (adjust the media queries based on your actual needs)
PWA_APP_SPLASH_SCREEN = [
    {
        'src': 'static/images/logo-512.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]

# New: Adding screenshots from the JSON
PWA_APP_SCREENSHOTS = [
    {
        'src': 'static/images/screenshot-wide.png',
        'sizes': '640x480',  # Matching size from the JSON
        'type': 'image/png',
        'form_factor': 'wide'  # Adding form factor
    },
    {
        'src': 'static/images/screenshot-narrow.png',
        'sizes': '360x640',  # Matching size from the JSON
        'type': 'image/png',
        'form_factor': 'narrow'  # Adding form factor
    }
]

PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
