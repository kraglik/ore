from typing import Tuple, Any

from ore_combinators.combinator import combinator
from ore_combinators.parser_state import ParserState
from ore_combinators.result import Result
from ore_combinators.error import ParserError, EndOfFileError


class string(combinator):   # noqa
    def __init__(self, s: str):
        self._string = s

    def __call__(self, state: ParserState) -> Tuple[Any, ParserState]:
        initial_state = state

        for char in self._string:
            if state.is_at_end():
                raise EndOfFileError(position=initial_state.position)

            if char != state.symbol:
                raise ParserError(
                    message="String mismatch",
                    position=initial_state.position
                )

            state = state.next()

        return Result.make_value(self._string, state)
