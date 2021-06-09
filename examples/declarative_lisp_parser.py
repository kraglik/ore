from typing import Tuple

from ore.combinators import *
from ore import ParserState, Result, ParserError, Source
from examples.lisp_ast import *


def list_of_symbols_to_name(l):
    return NameNode(''.join(l))


def list_of_elements_to_string(l):
    return join_list(l[1])


left = symbol('(')
right = symbol(')')

join_list = lambda l: ''.join(l)    # noqa

name_allowed_symbols = alt(one_of_symbols(['-', '_', '?']), alphabet)

name = transform(
    sequence(
        name_allowed_symbols,
        transform(
            take_while_possible(name_allowed_symbols),
            join_list
        )
    ),
    list_of_symbols_to_name
)

string_part = transform(
    alt(
        string('\"'),
        string('\\"'),
        any_symbol()
    ),
    join_list
)

string_parser = transform(
    sequence(
        symbol('"'),
        take_until(
            string_part,
            symbol('"')
        ),
        symbol('"')
    ),
    list_of_elements_to_string
)

float_parser = transform(
    sequence(
        transform(
            take_while(
                any_symbol(),
                digits,
            ),
            join_list,
        ),
        symbol('.'),
        transform(
            take_while(
                any_symbol(),
                digits
            ),
            join_list
        )
    ),
    lambda l: FloatNumber(float(l.join('')))
)

integer_parser = transform(
    take_while(
        any_symbol(),
        digits,
    ),
    lambda l: IntNumber(int(join_list(l))),
)

number_parser = alt(
    float_parser,
    integer_parser
)

value_parser = alt(
    string_parser,
    number_parser
)

value_or_name = alt(
    value_parser,
    name
)

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


list_parser = transform(
    sequence(
        left,
        take_while_possible(
            transform(
                sequence(
                    empty_symbol_eater,
                    value_parser,
                ),
                lambda l: l[1]
            )
        ),
        empty_symbol_eater,
        right
    ),
    lambda l: ListNode(l[1])
)


def app_parser():
    return transform(
        sequence(
            empty_symbol_eater,
            left,
            name,
            transform(
                take_while_possible(
                    sequence(
                        empty_symbol_eater,
                        alt(
                            list_parser,
                            app_parser,
                            value_or_name
                        )
                    )
                ),
                lambda l: [i for sl in l for i in sl if isinstance(i, LispASTNode)]
            ),
            empty_symbol_eater,
            right,
            empty_symbol_eater
        ),
        lambda l: Application(l[2], l[3])
    )
