from typing import Tuple

from ore_combinators.combinators import *
from ore_combinators import ParserState, Result, ParserError, Source, combinator_function
from examples.lisp_ast import *


def list_of_symbols_to_name(l):
    return NameNode(''.join(l))


def list_of_elements_to_string(l):
    return join_list(l[1])


left = symbol('(')
right = symbol(')')

join_list = lambda l: ''.join(l)    # noqa

name_allowed_symbols = alt(one_of_symbols('-_?+/*^%#@!<>'), alphabet)


@combinator_function()
def parse_name(state):
    first_symbol, state = name_allowed_symbols(state)
    other_symbols, state = take_while_possible(name_allowed_symbols)(state)

    return Result.make_value(
        NameNode(first_symbol + ''.join(other_symbols)),
        state
    )


@combinator_function()
def parse_int(state):
    int_digits, state = take_while_possible(digits)(state)

    return Result.make_value(IntNumber(int(''.join(int_digits))), state)


@combinator_function()
def parse_float(state):
    integral_part, state = take_while_possible(digits)(state)
    _, state = symbol('.')(state)
    fractional_part, state = take_while_possible(digits)(state)

    return Result.make_value(
        FloatNumber(float(f'{"".join(integral_part)}.{"".join(fractional_part)}')),
        state
    )


@combinator_function()
def parse_string(state):
    _, state = symbol('"')(state)

    string_result, state = take_until(
        alt(
            string('\"'),
            string('\\"'),
            any_symbol()
        ),
        symbol('"')
    )(state)

    _, state = symbol('"')(state)

    return Result.make_value(
        String(''.join(string_result)),
        state
    )


parse_value = alt(parse_float, parse_int, parse_string)
whitespace_eater = take_while(any_symbol(), one_of_symbols([' ', '\t']))
empty_line_eater = take_while(
    any_symbol(),
    sequence(
        whitespace_eater,
        newline
    )
)
empty_symbol_eater = transform(
    take_while(
        any_symbol(),
        alt(
            newline,
            symbol(' '),
            symbol('\t')
        )
    ),
    lambda _: None
)


@combinator_function()
def parse_list(state):
    _, state = empty_symbol_eater(state)
    _, state = left(state)
    _, state = empty_symbol_eater(state)

    items, state = take_while_possible(
        transform(
            sequence(
                parse_value,
                empty_symbol_eater
            ),
            lambda l: l[0]
        )
    )(state)
    _, state = right(state)

    return Result.make_value(
        ListNode(items),
        state
    )


@combinator_function(custom_error=None)
def parse_app(state):
    _, state = empty_symbol_eater(state)
    _, state = left(state)
    _, state = empty_symbol_eater(state)
    fun_name, state = parse_name(state)
    _, state = empty_symbol_eater(state)

    items, state = take_while_possible(
        transform(
            sequence(
                alt(
                    parse_list,
                    parse_app,
                    parse_name,
                    parse_value
                ),
                empty_symbol_eater
            ),
            lambda l: l[0]
        )
    )(state)
    _, state = right(state)

    return Result.make_value(Application(fun_name, items), state)
