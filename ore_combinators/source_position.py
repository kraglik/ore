from typing import NewType


Row             = NewType('Row',            int)    # noqa
Column          = NewType('Column',         int)    # noqa
SymbolPosition  = NewType('SymbolPosition', int)    # noqa


class SourcePosition:
    def __init__(self, row: Row, column: Column, symbol: SymbolPosition):
        self._row = row
        self._column = column
        self._symbol = symbol

    @staticmethod
    def initial() -> 'SourcePosition':
        return SourcePosition(
            row=Row(1),
            column=Column(1),
            symbol=SymbolPosition(0)
        )

    @property
    def row(self) -> Row:
        return self._row

    @property
    def column(self) -> Column:
        return self._column

    @property
    def symbol(self) -> SymbolPosition:
        return self._symbol

    def __str__(self):
        return f'SourcePosition(row={int(self._row)}, column={int(self._column)}, symbol_position={int(self._symbol)})'
