from .alt import alt
from .any_symbol import any_symbol
from .symbol import symbol
from .take_n import take_n
from .sequence import sequence
from .one_of_symbols import one_of_symbols
from .string import string
from .take_until import take_until
from .take_while import take_while
from .safe import safe
from .transform import transform
from .take_while_possible import take_while_possible

digits = one_of_symbols('0123456789')
hex_digits = one_of_symbols('0123456789abcdefABCDEF')
lower_alphabet = one_of_symbols('abcdefghijklmnopqrstuvwxyz')
upper_alphabet = one_of_symbols('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alphabet = alt(lower_alphabet, upper_alphabet)
newline = one_of_symbols(['\n'])
