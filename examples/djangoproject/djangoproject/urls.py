from django.conf.urls import patterns, url, include

from django_view_timer.urls import (
   patterns as dvt_patterns,
   url as dvt_url
)

from .views import index, fun_base_test_view, ClassBaseTestView

original_urlpatterns = patterns('djangoproject.views',
   url(r'^$', index, name='index'),
)

dvt_urlpatterns = dvt_patterns('djangoproject.views',
   dvt_url(r'^dvt_fun_base_str$', 'fun_base_test_view', name='dvt_fb_str_view'),
   dvt_url(r'^dvt_fun_base$', fun_base_test_view, name='dvt_fb_view'),
   dvt_url(r'^dvt_class_base$', ClassBaseTestView.as_view(), name='dvt_cb_view'),
)

# urlpatterns = original_urlpatterns + dvt_urlpatterns
urlpatterns = patterns('',
    url(r'', include(original_urlpatterns)),
    url(r'dvt/', include(dvt_urlpatterns)),
)
