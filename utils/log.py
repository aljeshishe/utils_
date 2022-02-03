import functools
import logging


log = logging.getLogger(__name__)


def trace(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        log.debug(f.__name__, args, kwargs)
        return f(*args, **kwargs)
    return wrapper

