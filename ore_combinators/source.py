from ore_combinators.source_span import SourceSpan, SourcePosition


class Source:
    def __init__(self, text: str):
        self._text = text

    def text_in_span(self, span: SourceSpan) -> str:
        return self._text[span.first_symbol_position: span.last_symbol_position]

    def symbol_at(self, source_position: SourcePosition) -> str:
        return self._text[source_position.symbol]

    def __len__(self):
        return len(self._text)
