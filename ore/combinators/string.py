from typing import Tuple, Any

from ore.combinator import combinator
from ore.parser_state import ParserState
from ore.result import Result
from ore.error import ParserError, EndOfFileError


class StringError(ParserError):
    pass


class string(combinator):   # noqa
    def __init__(self, s: str):
        self._string = s

    def __call__(self, state: ParserState) -> Tuple[Any, ParserState]:
        initial_state = state

        for char in self._string:
            if state.is_at_end():
                raise EndOfFileError(position=initial_state.position)

            if char != state.symbol:
                raise StringError(
                    message="String mismatch",
                    position=initial_state.position
                )

            state = state.next()

        return Result.make_value(self._string, state)
