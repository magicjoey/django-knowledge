import os

import dj_database_url

DIRNAME = os.path.dirname(__file__)

DEBUG = True

DATABASES = {'default': dj_database_url.config(default='mysql://root:@127.0.0.1:3306/knowledge')}

STATIC_URL = '/static/'

INTERNAL_IPS = ('127.0.0.1',)

SITE_ID = 1
SECRET_KEY = 'lolz'

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    # 多站点
    'django.contrib.sites',

    'debug_toolbar',
    'knowledge',
    # 'south',
    'django_coverage',
    'mock',
)


ROOT_URLCONF = 'tests.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(DIRNAME, 'templates').replace('\\', '/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static'
            ],
        },
    },
]

TIME_ZONE = 'Asia/Shanghai'
USE_TZ = True

ALLOWED_HOSTS = ['127.0.0.1']

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(DIRNAME, 'reports').replace('\\','/')

LOGIN_REDIRECT_URL = '/admin/'

SITE_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')

STATIC_ROOT = os.path.join(SITE_ROOT, 'knowledge/static/knowledge')

STATICFILES_DIRS = (
    ("css", os.path.join(STATIC_ROOT, 'css')),
    ("scss", os.path.join(STATIC_ROOT, 'scss')),
)
