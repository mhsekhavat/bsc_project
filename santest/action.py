def action(func):
    def wrapper(**kwargs):
        tests = filter(lambda test: test.when(func, **kwargs) and test.given(**kwargs), all_tests)
        ret = func(**kwargs)
        for test in tests:
            test.then(return_value=ret, **kwargs)

    return wrapper
