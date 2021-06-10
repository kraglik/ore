from typing import Tuple, Any

from ore_combinators.combinator import combinator, Combinator
from ore_combinators.parser_state import ParserState
from ore_combinators.result import Result
from ore_combinators.error import ParserError, EndOfFileError


class sequence(combinator):   # noqa
    def __init__(self, *combinators: Combinator):
        self._combinators = combinators

    def __call__(self, state: ParserState) -> Tuple[Any, ParserState]:
        results = []

        for c in self._combinators:
            try:
                result, state = c(state)
            except EndOfFileError:
                continue
            except ParserError as e:
                raise ParserError(
                    message="Error while processing sequence",
                    position=state.position,
                    nested_error=e
                )

            results.append(result)

        return Result.make_value(results, state)
