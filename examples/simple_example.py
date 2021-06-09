from typing import Tuple

from ore_combinators.combinators import *
from ore_combinators import ParserState, Result, ParserError, Source


abc_parser = sequence(
    symbol('A'),
    symbol('B'),
    symbol('C')
)

abbbc_parser = sequence(
    symbol('A'),
    take_n(3, symbol('B')),
    symbol('C')
)

a___c_parser = sequence(
    symbol('A'),
    take_n(3, any_symbol()),
    symbol('C')
)

module_keyword = string('module')
whitespace_eater = take_while(any_symbol(), symbol(' '))

module_parser = sequence(
    module_keyword,
    whitespace_eater,
    transform(
        take_until(any_symbol(), symbol('\n')),
        lambda l: ''.join(l)
    )
)

all_parser = safe(
    alt(
        abc_parser,
        abbbc_parser,
        a___c_parser,
        module_parser
    )
)


def main():
    text = "ABC"
    text2 = "DEF"
    text3 = "ABBBC"
    text4 = "ALOLC"
    text5 = """module Lambda
    aaaa
    """

    state1 = ParserState(Source(text))
    state2 = ParserState(Source(text2))
    state3 = ParserState(Source(text3))
    state4 = ParserState(Source(text4))
    state5 = ParserState(Source(text5))

    result1, _ = all_parser(state1)
    result2, _ = all_parser(state2)
    result3, _ = all_parser(state3)
    result4, _ = all_parser(state4)
    result5, _ = all_parser(state5)

    print(result1.error)
    print(result2.error)
    print(result3.error)
    print(result4.error)
    print(result5.error)

    print('#' * 100)

    print(result1.value)
    print(result2.value)
    print(result3.value)
    print(result4.value)
    print(result5.value)

    print('#' * 100)

    r, _ = take_until(any_symbol(), string('bc'))(ParserState(Source('aaaabc')))
    print(r.value)
    print(r.error)


if __name__ == '__main__':
    main()
