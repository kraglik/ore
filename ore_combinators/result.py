class Result:
    def __init__(self, value=None, error=None):
        self._value = value
        self._error = error

    def is_ok(self) -> bool:
        return self._error is None

    def is_error(self) -> bool:
        return self._error is not None

    @property
    def value(self):
        return self._value

    @property
    def error(self):
        return self._error

    @staticmethod
    def make_value(value, state):
        return value, state

    @staticmethod
    def make_error(error, state):
        return Result(value=None, error=error), state
