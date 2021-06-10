from typing import Tuple, Union, Any, Callable

from ore_combinators.combinator import combinator, Combinator
from ore_combinators.error import ParserError
from ore_combinators.parser_state import ParserState
from ore_combinators.result import Result


class alt(combinator):  # noqa
    def __init__(self, *combinators: Combinator):
        self._combinators = list(combinators)

    def __call__(self, state: ParserState) -> Tuple[Any, ParserState]:
        for c in self._combinators:
            try:
                result, new_state = c(state)
            except Exception:
                continue

            return result, new_state

        raise ParserError(message='Match not found', position=state.position)
