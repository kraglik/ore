# Ore

A simple WIP pythonic parser combinator library inspired by Haskell's attoparsec.

It supports two styles: declarative and imperative.

For example, declarative style looks like the following:
```python3
from ore.combinators import alphabet, transform
from ore.combinators import sequence, take_while_possible

join = lambda l: ''.join(l)

name = transform(
    sequence(
        alphabet,
        transform(
            take_while_possible(alphabet),
            join
        )
    ),
    join
)
```

The very same combinator could be written as function:
```python3
from typing import Tuple

from ore.combinators import alphabet
from ore.combinators import take_while_possible
from ore import combinator_function, ParserState, Result


@combinator_function()
def name(state: ParserState) -> Tuple[Result, ParserState]:
    first_symbol, state = alphabet(state)
    other_symbols, state = take_while_possible(alphabet)(state)

    return Result.make_value(
        first_symbol.value + ''.join(other_symbols.value),
        state
    )
```

To run a parser on a given text, use `run` or `run_safe`:

```python3
from typing import Tuple

from ore.combinators import alphabet
from ore.combinators import take_while_possible
from ore import ParserState, Result
from ore import run_safe, combinator_function


@combinator_function()
def name(state: ParserState) -> Tuple[Result, ParserState]:
    first_symbol, state = alphabet(state)
    other_symbols, state = take_while_possible(alphabet)(state)

    return Result.make_value(
        first_symbol.value + ''.join(other_symbols.value),
        state
    )

name_result = run_safe(name, "Ore     ")

assert name_result.value == "Ore"
```

The difference between `run` and `run_safe` is that `run_safe` returns result without raising exceptions.
Exceptions saved in the result instead.
`run` just throws exceptions without saving them into result.

# Installation

To install this library, just type `pip install ore-combinators` in the console.
