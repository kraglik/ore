from typing import Tuple, Any

from ore.combinator import combinator
from ore.parser_state import ParserState
from ore.result import Result
from ore.error import ParserError, EndOfFileError


class AnySymbolError(ParserError):
    pass


class any_symbol(combinator):   # noqa
    def __call__(self, state: ParserState) -> Tuple[Any, ParserState]:
        if state.is_at_end():
            raise EndOfFileError(position=state.position)

        return Result.make_value(state.symbol, state.next())
