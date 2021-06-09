from typing import Union, Tuple

from ore_combinators.combinators import safe
from ore_combinators import Source, ParserState, combinator, Result


def run(parser: Union[callable, combinator], text: str) -> Result:
    result, _ = parser(ParserState(Source(text)))

    return Result(value=result)


def run_safe(parser: Union[callable, combinator], text: str) -> Result:
    result, _ = safe(parser)(ParserState(Source(text)))

    return result
