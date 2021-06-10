from typing import Optional, Union
from ore_combinators.source_position import SourcePosition


class ParserError(Exception):
    def __init__(
            self,
            message: str,
            position: SourcePosition,
            nested_error: Optional[Union[Exception, 'ParserError']] = None
    ):
        super().__init__(message)
        self._message = message
        self._position = position
        self._nested_error = nested_error

    @property
    def message(self) -> str:
        return self._message

    @property
    def position(self) -> SourcePosition:
        return self._position

    @property
    def nested_error(self) -> Union['ParserError', Exception]:
        return self._nested_error

    def __str__(self):
        return f'{self.__class__.__name__}' \
               f'(' \
               f'message="{self._message}", ' \
               f'position={self._position}, ' \
               f'nested_error={self._nested_error})'


class EndOfFileError(ParserError):
    def __init__(self, position):
        super().__init__('Unexpected EOF', position)
