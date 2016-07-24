import functools

from insanity.apps import all_checks


def action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        checks = map(lambda c: c(), all_checks)
        checks = filter(lambda check: check.when(*args, func=func, **kwargs) and check.given(*args, **kwargs), checks)
        checks = list(checks) # filter and map are lazy!
        ret = func(*args, **kwargs)
        for check in checks:
            check.then(*args, return_value=ret, **kwargs)
        return ret

    return wrapper
