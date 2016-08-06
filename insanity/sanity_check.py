class SanityCheck(object):
    action_name = None

    def __init__(check, action):
        check.action = action

    def given(check, **payload):
        return True

    def when(check, **payload):
        return True

    def then(check, exc_type, exc_val, exc_tb, return_value, payload):
        assert exc_type is None
