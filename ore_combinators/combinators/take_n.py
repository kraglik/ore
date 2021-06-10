from typing import Tuple, Any

from ore_combinators.combinator import combinator, Combinator
from ore_combinators.parser_state import ParserState
from ore_combinators.result import Result
from ore_combinators.error import ParserError, EndOfFileError


class take_n(combinator):   # noqa
    def __init__(self, amount: int, c: Combinator):
        self._amount = amount
        self._combinator = c

    def __call__(self, state: ParserState) -> Tuple[Any, ParserState]:
        output = []

        initial_state = state

        for i in range(self._amount):
            if state.is_at_end():
                raise EndOfFileError(initial_state.position)

            try:
                result, state = self._combinator(state)
            except ParserError as e:
                raise ParserError(message="Can't tale n elements", position=state.position, nested_error=e)

            output.append(result)

        return Result.make_value(output, state)
