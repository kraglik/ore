from typing import Tuple, Union, Any, Callable

from ore_combinators.combinator import combinator, Combinator
from ore_combinators.parser_state import ParserState
from ore_combinators.result import Result
from ore_combinators.error import ParserError, EndOfFileError


class take_until(combinator):   # noqa
    def __init__(self, c: Combinator, condition: Union[Combinator, Callable[[Any], bool]]):
        self._condition = condition
        self._combinator = c

    def __call__(self, state: ParserState) -> Tuple[Any, ParserState]:
        output = []

        initial_state = state
        previous_state = state

        while True:
            if state.is_at_end():
                break

            if isinstance(self._condition, combinator):
                must_break = True
                try:
                    self._condition(state)
                except ParserError:
                    must_break = False

                if must_break:
                    break

            previous_state = state

            try:
                result, state = self._combinator(state)
            except EndOfFileError:
                break

            except ParserError as e:
                raise ParserError(
                    message='TakeUntil error',
                    position=initial_state.position,
                    nested_error=e
                )

            if not isinstance(self._condition, combinator) and self._condition(result):
                break

            output.append(result)

        return Result.make_value(
            output,
            state if isinstance(self._condition, combinator) else previous_state
        )
