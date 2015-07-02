from django.conf.urls import url as django_url

from django_view_timer.profiler import ViewTimeProfiler
from django_view_timer.settings import DJANGO_VIEW_TIMER_ENABLED


def url(regex, view, kwargs=None, name=None, prefix=''):
    if DJANGO_VIEW_TIMER_ENABLED:
        view = ViewTimeProfiler(view)
    return django_url(regex, view, kwargs, name, prefix)
