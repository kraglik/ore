from ore_combinators.source import Source
from ore_combinators.source_position import SourcePosition, Row, Column, SymbolPosition


class ParserState:
    def __init__(
            self,
            source: Source,
            position: SourcePosition = SourcePosition.initial()
    ):
        self._source = source
        self._position = position

    def is_at_end(self) -> bool:
        return self._position.symbol == len(self._source)

    def next(self) -> 'ParserState':
        if self._source.symbol_at(self._position) == '\n':
            row = Row(self._position.row + 1)
            column = Column(1)
        else:
            row = Row(self._position.row)
            column = Column(self._position.column + 1)

        return ParserState(
            source=self._source,
            position=SourcePosition(
                row=row,
                column=column,
                symbol=SymbolPosition(self._position.symbol + 1)
            )
        )

    @property
    def position(self) -> SourcePosition:
        return self._position

    @property
    def symbol(self) -> str:
        return self._source.symbol_at(self._position)

