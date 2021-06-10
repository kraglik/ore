from typing import Union, List, Tuple, Any

from ore_combinators.combinator import combinator
from ore_combinators.parser_state import ParserState
from ore_combinators.result import Result
from ore_combinators.error import ParserError


class one_of_symbols(combinator):   # noqa
    def __init__(self, symbols: Union[List[str], Tuple[str], str]):
        self._symbols = symbols

    def __call__(self, state: ParserState) -> Tuple[Any, ParserState]:
        symbol = state.symbol

        if symbol not in self._symbols:
            raise ParserError(
                message='No symbol matched',
                position=state.position
            )

        return Result.make_value(symbol, state.next())

