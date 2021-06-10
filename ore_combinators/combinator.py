from typing import Tuple, Any, Callable, Optional, Union
from abc import abstractmethod

from ore_combinators.parser_state import ParserState
from ore_combinators.error import ParserError

CombinatorFunction = Callable[[ParserState], Tuple[Any, ParserState]]


class combinator:   # noqa
    @abstractmethod
    def __call__(self, state: ParserState) -> Tuple[Any, ParserState]:
        raise NotImplementedError


def combinator_function(custom_error: Optional[str] = None):
    def d(f: Combinator):
        def g(state: ParserState):
            if custom_error is not None:
                try:
                    return f(state)
                except ParserError as e:
                    raise ParserError(message=custom_error, position=state.position, nested_error=e)
            else:
                return f(state)

        g.is_combinator = True
        return g
    return d


Combinator = Union[CombinatorFunction, combinator]
