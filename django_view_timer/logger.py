import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('django_view_timer - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
