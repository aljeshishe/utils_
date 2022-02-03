import contextlib
import logging


log = logging.getLogger(__name__)


@contextlib.contextmanager
def supress():
    try:
        yield
    except Exception:
        log.exception('Exception raised')