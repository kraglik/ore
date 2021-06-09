from typing import Tuple, Any
from abc import abstractmethod

from ore_combinators.parser_state import ParserState
from ore_combinators.result import Result


class combinator:   # noqa
    @abstractmethod
    def __call__(self, state: ParserState) -> Tuple[Any, ParserState]:
        raise NotImplementedError


def combinator_function(custom_error=None):
    def d(f):
        def g(*args, **kwargs):
            if custom_error is not None:
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    raise custom_error(e)
            else:
                return f(*args, **kwargs)

        g.is_combinator = True
        return g
    return d
