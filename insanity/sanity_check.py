class SanityCheck(object):
    action_name = None

    def __init__(check, action):
        check.action = action

    def given(check, **kwargs):
        return True

    def when(check, **kwargs):
        return True

    def then(check, exc_type, **kwargs):
        assert exc_type is None
