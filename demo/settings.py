"""This file has the settings for Gstudio Demo"""
import os

gettext = lambda s: s

DEBUG = True

DATABASES = {'default':
             {'ENGINE': 'django.db.backends.sqlite3',
              'NAME': os.path.join(os.path.dirname(__file__), 'demo.db')}
             }

STATIC_URL = '/static/'

MEDIA_URL = '/static'
MEDIA_ROOT = '/static'


ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

SECRET_KEY = 'jo-1rzm(%sf)3#n+fb7h955yu$3(pt63abhi12_t7e^^5q8dyw'

USE_I18N = True
USE_L10N = True

SITE_ID = 1

LANGUAGE_CODE = 'en'

GRAPPELLI_ADMIN_TITLE = "Gnowledge Studio"

GRAPPELLI_INDEX_DASHBOARD = "demo.dashboard.CustomIndexDashboard"


# Authentication related
ACCOUNT_ACTIVATION_DAYS = 2
EMAIL_HOST = 'localhost'
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
LOGIN_REDIRECT_URL = '/'



LANGUAGES = (('en', gettext('English')),
             ('fr', gettext('French')),
             ('de', gettext('German')),
             ('es', gettext('Spanish')),
             ('it', gettext('Italian')),
             ('nl', gettext('Dutch')),
             ('hu', gettext('Hungarian')),
             ('ru', gettext('Russian')),
             ('pl', gettext('Polish')),
             ('pt_BR', gettext('Brazilian Portuguese')),
             ('zh_CN', gettext('Simplified Chinese')),)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    )

ROOT_URLCONF = 'demo.urls'

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader',
        )
     ),
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'gstudio.context_processors.version',
    'objectapp.context_processors.version',
    )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sitemaps',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'mptt',
    'reversion',
    'gstudio',
    'objectapp',
    'tagging',
    'django_xmlrpc',
    'djangoratings',
    'registration',
    'demo',
    )

from gstudio.xmlrpc import GSTUDIO_XMLRPC_METHODS
XMLRPC_METHODS = GSTUDIO_XMLRPC_METHODS

