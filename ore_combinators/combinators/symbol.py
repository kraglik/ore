from typing import Tuple, Any

from ore_combinators.combinator import combinator
from ore_combinators.parser_state import ParserState
from ore_combinators.result import Result
from ore_combinators.error import ParserError, EndOfFileError


class symbol(combinator):   # noqa
    def __init__(self, s: str):
        self._symbol = s

    def __call__(self, state: ParserState) -> Tuple[Any, ParserState]:
        if state.is_at_end():
            raise EndOfFileError(position=state.position)

        s = state.symbol

        if s != self._symbol:
            raise ParserError(
                message=f"Symbol mismatch ( expected: '{self._symbol}', got: '{s}' )",
                position=state.position
            )

        return Result.make_value(s, state.next())
