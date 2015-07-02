import warnings

from django.core.urlresolvers import ResolverMatch
from django.core.urlresolvers import (
    RegexURLPattern as DjangoRegexURLPattern,
    RegexURLResolver
)
from django.core.exceptions import ImproperlyConfigured
from django.utils import six
from django.utils.deprecation import RemovedInDjango20Warning

from django_view_timer.profiler import ViewTimeProfiler
from django_view_timer.settings import DJANGO_VIEW_TIMER_ENABLED


class RegexURLPattern(DjangoRegexURLPattern):
    def resolve(self, path):
        match = self.regex.search(path)
        if match:
            kwargs = match.groupdict()
            if kwargs:
                args = ()
            else:
                args = match.groups()
            kwargs.update(self.default_args)
            callback = ViewTimeProfiler(self.callback) if DJANGO_VIEW_TIMER_ENABLED else self.callback
            return ResolverMatch(callback, args, kwargs, self.name)


def url(regex, view, kwargs=None, name=None, prefix=''):
    if isinstance(view, (list, tuple)):
        urlconf_module, app_name, namespace = ViewTimeProfiler(view) if DJANGO_VIEW_TIMER_ENABLED else view
        return RegexURLResolver(regex, urlconf_module, kwargs, app_name=app_name, namespace=namespace)
    else:
        if isinstance(view, six.string_types):
            warnings.warn(
                'Support for string view arguments to url() is deprecated and '
                'will be removed in Django 2.0 (got %s). Pass the callable '
                'instead.' % view,
                RemovedInDjango20Warning, stacklevel=2
            )
            if not view:
                raise ImproperlyConfigured('Empty URL pattern view name not permitted (for pattern %r)' % regex)
            if prefix:
                view = prefix + '.' + view
        return RegexURLPattern(regex, view, kwargs, name)


def patterns(prefix, *args):
    pattern_list = []
    for t in args:
        if isinstance(t, (list, tuple)):
            t = url(prefix=prefix, *t)
        elif isinstance(t, RegexURLPattern):
            t.add_prefix(prefix)
        pattern_list.append(t)
    return pattern_list
