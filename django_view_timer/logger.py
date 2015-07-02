import logging
import sys

from termcolor import cprint


class ColorLog(object):
    colormap = dict(
        info=dict(color='cyan', attrs=['bold']),
        warning=dict(color='white', on_color='on_red', attrs=['bold']),
    )

    def __init__(self, logger):
        self._log = logger

    def __getattr__(self, name):
        if name in ['info', 'warning']:
            return lambda s, *args: getattr(self._log, name)(
                cprint(s, **self.colormap[name]), *args)
        return getattr(self._log, name)


logger = ColorLog(logging.getLogger(__name__))

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('django_view_timer - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
