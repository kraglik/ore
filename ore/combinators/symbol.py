from typing import Tuple, Any

from ore.combinator import combinator
from ore.parser_state import ParserState
from ore.result import Result
from ore.error import ParserError, EndOfFileError


class SymbolError(ParserError):
    pass


class symbol(combinator):   # noqa
    def __init__(self, s: str):
        self._symbol = s

    def __call__(self, state: ParserState) -> Tuple[Any, ParserState]:
        if state.is_at_end():
            raise EndOfFileError(position=state.position)

        s = state.symbol

        if s != self._symbol:
            raise SymbolError(message='Symbol mismatch', position=state.position)

        return Result.make_value(s, state.next())
