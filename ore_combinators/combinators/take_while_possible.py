from typing import Tuple, Union, Any

from ore_combinators.combinator import combinator
from ore_combinators.parser_state import ParserState
from ore_combinators.result import Result
from ore_combinators.error import ParserError, EndOfFileError


class take_while_possible(combinator):   # noqa
    def __init__(self, c: combinator):
        self._combinator = c

    def __call__(self, state: ParserState) -> Tuple[Any, ParserState]:
        output = []

        while True:
            if state.is_at_end():
                break

            try:
                result, state = self._combinator(state)

            except ParserError:
                break

            output.append(result)

        return Result.make_value(output, state)
