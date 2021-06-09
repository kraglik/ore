from typing import Tuple

from ore.combinator import combinator
from ore.error import ParserError
from ore.parser_state import ParserState
from ore.result import Result


class safe(combinator):  # noqa
    def __init__(self, c: combinator):
        self._combinator = c

    def __call__(self, state: ParserState) -> Tuple[Result, ParserState]:
        try:
            result, new_state = self._combinator(state)
        except Exception as e:
            return Result.make_error(e, state)

        return Result(value=result), new_state
