from typing import Union, List, Tuple

from ore.combinator import combinator
from ore.parser_state import ParserState
from ore.result import Result
from ore.error import ParserError


class OneOfSymbolsError(ParserError):
    pass


class one_of_symbols(combinator):   # noqa
    def __init__(self, symbols: Union[List[str], Tuple[str], str]):
        self._symbols = symbols

    def __call__(self, state: ParserState) -> Tuple[Result, ParserState]:
        symbol = state.symbol

        if symbol not in self._symbols:
            raise OneOfSymbolsError(
                message='No symbol matched',
                position=state.position
            )

        return Result.make_value(symbol, state.next())

