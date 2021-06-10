from typing import Tuple, Union

from ore_combinators.combinator import combinator, Combinator
from ore_combinators.error import ParserError
from ore_combinators.parser_state import ParserState
from ore_combinators.result import Result


class safe(combinator):  # noqa
    def __init__(self, c: Combinator):
        self._combinator = c

    def __call__(self, state: ParserState) -> Tuple[Result, ParserState]:
        try:
            result, new_state = self._combinator(state)
        except Exception as e:
            return Result.make_error(e, state)

        return Result(value=result), new_state
