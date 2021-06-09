from typing import Tuple

from ore_combinators.source_position import SourcePosition, SymbolPosition, Row, Column


class SourceSpan:
    def __init__(self, start_pos: SourcePosition, end_pos: SourcePosition):
        self._start_pos = start_pos
        self._end_pos = end_pos

    @property
    def first_symbol_position(self) -> SymbolPosition:
        return self._start_pos.symbol

    @property
    def last_symbol_position(self) -> SymbolPosition:
        return self._end_pos.symbol

    @property
    def start_row_column(self) -> Tuple[Row, Column]:
        return self._start_pos.row, self._start_pos.column
