from typing import Tuple, Any

from ore_combinators.combinator import combinator
from ore_combinators.parser_state import ParserState
from ore_combinators.result import Result
from ore_combinators.error import ParserError, EndOfFileError


class any_symbol(combinator):   # noqa
    def __call__(self, state: ParserState) -> Tuple[Any, ParserState]:
        if state.is_at_end():
            raise EndOfFileError(position=state.position)

        return Result.make_value(state.symbol, state.next())
