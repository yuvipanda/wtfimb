import os.path
# Django settings for wtfimb project.

ROOT_DIR = os.path.dirname(__file__)

import localsettings

DEBUG = localsettings.DEBUG
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS


DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = localsettings.DATABASE_NAME             # Or path to database file if using sqlite3.
DATABASE_USER = localsettings.DATABASE_USER             # Not used with sqlite3.
DATABASE_PASSWORD = localsettings.DATABASE_PASSWORD         # Not used with sqlite3.
DATABASE_HOST = localsettings.DATABASE_HOST             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = localsettings.DATABASE_PORT             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Calcutta'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

STATIC_DOC_ROOT = os.path.join(ROOT_DIR, 'static').replace('\\','/')

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'hs#xo8_e6hxi747-vz_7!=xzui*!$#ds3)x-hxfpfqc704edxd'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
        'django.core.context_processors.auth',
        )

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'wtfimb.urls'

TEMPLATE_DIRS = (
        os.path.join(ROOT_DIR, 'templates').replace('\\','/'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.humanize',

    'wtfimb.routing',
    'wtfimb.home',
    'wtfimb.routes',
    'wtfimb.stages',
    
    'registration',
)

GRAPH_CACHE = os.path.join(ROOT_DIR, 'graph')

#Number of Days Activate Link is valid
ACCOUNT_ACTIVATION_DAYS = 30

# Email Settings

EMAIL_HOST = localsettings.EMAIL_HOST
EMAIL_HOST_USER = localsettings.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = localsettings.EMAIL_HOST_PASSWORD

DEFAULT_FROM_EMAIL = 'admin@busroutes.in'

# Caching
CACHE_BACKEND = localsettings.CACHE_BACKEND
