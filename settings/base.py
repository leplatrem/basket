import os
import sys

# Application version.
VERSION = (0, 1)

# Make filepaths relative to settings.
ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS':  {'init_command': 'SET storage_engine=InnoDB'},
    }
}

ALLOWED_HOSTS = [
    '.allizom.org',
    'basket.mozilla.com',
    'basket.mozilla.org',
]

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True

MEDIA_ROOT = path('media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0D8AE44F-5714-40EF-9AC8-4AC6EB556161'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'csrf_context.csrf',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'news.middleware.GraphiteViewHitCountMiddleware',
    'django_statsd.middleware.GraphiteMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    path('templates'),
)

INSTALLED_APPS = (
    'news',

    'djcelery',
    'south',
    'raven.contrib.django.raven_compat',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
)

if 'test' in sys.argv:
    INSTALLED_APPS += ('django_nose',)

LANGUAGES = (
    'af','ak','ast-ES','ar','as','be','bg','bn-BD','bn-IN','br-FR',
    'ca','ca-valencia','cs','cy','da','de','de-AT','de-CH','de-DE',
    'dsb','el','en-AU','en-CA','en-GB','en-NZ','en-US','en-ZA','eo',
    'es','es-AR','es-CL','es-ES','es-MX','et','eu','fa','fi','fj-FJ',
    'fr','fur-IT','fy-NL','ga','ga-IE','gl','gu-IN','he','hi','hi-IN',
    'hr','hsb','hu','hy-AM','id','is','it','ja','ja-jp','ja-JP-mac','ka','kk',
    'kn','ko','ku','la','lt','lv','mg','mi','mk','ml','mn','mr','nb-NO',
    'ne-NP','nn-NO','nl','nr','nso','oc','or','pa-IN','pl','pt-BR','pt-PT',
    'ro','rm','ru','rw','si','sk','sl','sq','sr','sr-Latn','ss','st',
    'sv-SE','ta','ta-IN','ta-LK','te','th','tn','tr','ts','tt-RU','uk','ur',
    've','vi','wo','xh','zh-CN','zh-TW','zu',)
LANGUAGES_LOWERED = [x.lower() for x in LANGUAGES]

DEFAULT_FROM_EMAIL = 'basket@mozilla.com'
DEFAULT_FROM_NAME = 'Mozilla'

# LDAP
LDAP = {
    'host': '',
    'port': '',
    'user': '',
    'password': '',
    'search_base': 'o=com,dc=mozilla',
}

EMAIL_BACKEND = 'mysmtp.EmailBackend'
EMAIL_BACKLOG_TOLERANCE = 200
SYNC_UNSUBSCRIBE_LIMIT = 1000
LDAP_TIMEOUT = 2

# Default newsletter welcome message ID for HTML format.
# There must also exist a text-format message with the same
# ID with "_T" appended, e.g. "39_T"
DEFAULT_WELCOME_MESSAGE_ID = '39'

# Name of the database where we put someone's token when they confirm
EXACTTARGET_CONFIRMATION = 'Confirmation'

# This is a token that bypasses the news app auth in certain ways to
# make debugging easier
# SUPERTOKEN = <token>

# Uncomment these to use Celery, use eager for local dev
CELERY_ALWAYS_EAGER = False
BROKER_HOST = 'localhost'
BROKER_PORT = 5672
BROKER_USER = 'basket'
BROKER_PASSWORD = 'basket'
BROKER_VHOST = 'basket'
CELERY_DISABLE_RATE_LIMITS = True
CELERY_IGNORE_RESULT = True

import djcelery
djcelery.setup_loader()

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
