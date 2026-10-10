# Settings for container platforms: everything is read from the environment.
import os
from urllib.parse import unquote, urlparse

SECRET_KEY = os.environ['SECRET_KEY']
FIELD_ENCRYPTION_KEY = os.environ['FIELD_ENCRYPTION_KEY']

DEBUG = os.environ.get('DEBUG', '').lower() in ('1', 'true', 'yes')

ALLOWED_HOSTS = [h.strip() for h in os.environ.get('ALLOWED_HOSTS', '*').split(',') if h.strip()]
CSRF_TRUSTED_ORIGINS = [o.strip() for o in os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',') if o.strip()]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

PIPELINE_LOCAL = {}
PIPELINE_LOCAL['JS_COMPRESSOR'] = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
PIPELINE_LOCAL['CSS_COMPRESSOR'] = 'pipeline.compressors.cssmin.CSSMinCompressor'

LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'en-us')
TIME_ZONE = os.environ.get('TIME_ZONE', 'UTC')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_db_url = os.environ.get('DATABASE_URL')
if _db_url:
    _u = urlparse(_db_url)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': unquote(_u.path.lstrip('/')),
            'USER': unquote(_u.username or ''),
            'PASSWORD': unquote(_u.password or ''),
            'HOST': _u.hostname or '',
            'PORT': str(_u.port or 5432),
            'CONN_MAX_AGE': 60,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

INSTALLED_APPS_LOCAL = []
