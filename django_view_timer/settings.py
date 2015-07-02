"""
Settings for drf-chaos

DRF_CHAOS_ENABLED = True
"""
from django.conf import settings

DJANGO_VIEW_TIMER_ENABLED = getattr(settings, 'DJANGO_VIEW_TIMER_ENABLED', True)
DJANGO_VIEW_TIMER_THRESHOLD = getattr(settings, 'DJANGO_VIEW_TIMER_THRESHOLD', 9999)
DJANGO_VIEW_TIMER_LOG_FORMAT = getattr(settings, 'DJANGO_VIEW_TIMER_LOG_FORMAT',
                                       "Module: {module}\t"
                                       "Function: {function}\t"
                                       "Execution Time: {time} msecs")
