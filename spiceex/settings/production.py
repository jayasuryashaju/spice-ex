from .base import *

DEBUG = False

ALLOWED_HOSTS = ['spiceex.in', 'www.spiceex.in', '13.60.239.151']  

# Production database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'spiceex_db',
        'USER': 'spiceex',
        'PASSWORD': '9847227810@Aa',  
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Use the actual static and media file configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security settings
SECURE_HSTS_SECONDS = 3600  # Force HTTPS (still keep it for better security)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = False  # Allow both HTTP and HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# Additional settings for handling insecure requests (if necessary)
if not DEBUG:
    # Allow both http and https in production, but make sure to only use secure cookies
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


