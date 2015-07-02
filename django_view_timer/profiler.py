import datetime
import inspect

import wrapt

from .settings import (
    DJANGO_VIEW_TIMER_THRESHOLD,
    DJANGO_VIEW_TIMER_LOG_FORMAT,
)
from .logger import logger


class ViewTimeProfiler(wrapt.ObjectProxy):
    def __call__(self, *args, **kwargs):
        start = datetime.datetime.now()
        try:
            return self.__wrapped__(*args, **kwargs)
        finally:
            delta = datetime.datetime.now() - start
            module = inspect.getmodule(self.__wrapped__)
            msecs = float(delta.total_seconds() * 1000)
            if DJANGO_VIEW_TIMER_THRESHOLD <= msecs:
                logger.debug(DJANGO_VIEW_TIMER_LOG_FORMAT
                             .format(module=module.__name__,
                                     function=self.__wrapped__.__name__,
                                     time=msecs))
