from typing import Tuple, Union, Any

from ore_combinators.combinator import combinator
from ore_combinators.error import ParserError
from ore_combinators.parser_state import ParserState
from ore_combinators.result import Result


class AltError(ParserError):
    pass


class alt(combinator):  # noqa
    def __init__(self, *combinators: Union[combinator, callable]):
        self._combinators = list(combinators)

    def __call__(self, state: ParserState) -> Tuple[Any, ParserState]:
        for c in self._combinators:
            if not isinstance(c, combinator) and not hasattr(c, 'is_combinator'):
                c = c()

            try:
                result, new_state = c(state)
            except Exception:
                continue

            return result, new_state

        raise AltError(message='Match not found', position=state.position)
