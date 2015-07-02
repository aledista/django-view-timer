from django.conf.urls import patterns, url

from django_view_timer.urls import url as dvt_url

from .views import fun_base_test_view, ClassBaseTestView


urlpatterns = patterns('',
   url(r'fun_base$', fun_base_test_view, name='fb_view'),
   dvt_url(r'class_base$', ClassBaseTestView.as_view(), name='cb_view'),
)
