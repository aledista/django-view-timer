django-view-timer
===================
Profile execution time for django views

.. image:: https://img.shields.io/pypi/v/django-view-timer.svg

Settings
=========
None of the following settings are mandatory

|

``DJANGO_VIEW_TIMER_ENABLED``

Enable/Disable profiler

Default value: True

|

``DJANGO_VIEW_TIMER_MIN_THRESHOLD``

Disregards execution time below threshold (in milliseconds)

Default value: 10

|

``DJANGO_VIEW_TIMER_WARNING_LEVEL``

Set number of milliseconds for warnings

Default value: 300

|

``DJANGO_VIEW_TIMER_LOG_FORMAT``

Log Format

Default Value:
::

   "Module: {module}\tFunction: {function}\tExecution Time: {time} msecs"

Installation
============

Install using ``pip``\
::

    pip install django_view_timer

in urls.py import
::

    from django_view_timer.urls import url as dvt_url

    urlpatterns = patterns('',
      url(r'view$', fun_base_test_view, name='fbv_view'),
      dvt_url(r'profiled_view$', ClassBaseTestView.as_view(), name='cbv_view'),
    )
