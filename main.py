from examples.imperative_lisp_parser import *
from ore_combinators import run_safe


def main():
    text = """
    (add
        (head 
            (1 2 3))
        4)
    """
    result = run_safe(parse_app, text)

    print(result.value)


if __name__ == '__main__':
    main()
