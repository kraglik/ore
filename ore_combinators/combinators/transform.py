from typing import Tuple, Any

from ore_combinators.combinator import combinator
from ore_combinators.parser_state import ParserState
from ore_combinators.result import Result
from ore_combinators.error import ParserError


class TransformError(ParserError):
    pass


class transform(combinator):   # noqa
    def __init__(self, c: combinator, transformation_function: callable):
        self._combinator = c
        self._transformation_function = transformation_function

    def __call__(self, state: ParserState) -> Tuple[Any, ParserState]:

        try:
            combinator_result, new_state = self._combinator(state)
        except ParserError as e:
            raise TransformError(
                message='Result transformation error: failed to obtain a result',
                position=state.position,
                nested_error=e
            )

        return Result.make_value(self._transformation_function(combinator_result), new_state)
