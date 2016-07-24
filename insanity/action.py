def action(func):
    def wrapper(**kwargs):
        checks = filter(lambda check: check.when(func, **kwargs) and check.given(**kwargs), all_checks)
        ret = func(**kwargs)
        for check in checks:
            check.then(return_value=ret, **kwargs)
        return ret

    return wrapper
