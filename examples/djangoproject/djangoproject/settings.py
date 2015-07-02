import os

PROJECT_ROOT = os.path.dirname(__file__)

DEBUG = True
SECRET_KEY = 'kjdfh783de4r56nEyldskjf83'
ROOT_URLCONF = 'djangoproject.urls'

TEMPLATE_DIRS = [os.path.join(PROJECT_ROOT, 'templates')]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',

    'django_view_timer',
]

DJANGO_VIEW_TIMER_ENABLED = True
DJANGO_VIEW_TIMER_THRESHOLD = 450
DJANGO_VIEW_TIMER_LOG_FORMAT = "{module} {function} {time}"
