from typing import Tuple

from ore.combinator import combinator
from ore.parser_state import ParserState
from ore.result import Result
from ore.error import ParserError, EndOfFileError


class SequenceError(ParserError):
    pass


class sequence(combinator):   # noqa
    def __init__(self, *combinators: combinator):
        self._combinators = combinators

    def __call__(self, state: ParserState) -> Tuple[Result, ParserState]:
        results = []

        for c in self._combinators:
            try:
                result, state = c(state)
            except EndOfFileError:
                continue
            except ParserError as e:
                raise SequenceError(
                    message="Error while processing sequence",
                    position=state.position,
                    nested_error=e
                )

            results.append(result.value)

        return Result.make_value(results, state)
