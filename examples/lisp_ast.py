class LispASTNode:
    pass


class NameNode(LispASTNode):
    def __init__(self, n):
        self.name = n

    def __str__(self):
        return self.name


class Value(LispASTNode):
    def __init__(self, value):
        self.value = value


class IntNumber(Value):
    def __str__(self):
        return str(self.value)


class FloatNumber(Value):
    def __str__(self):
        return str(self.value)


class String(Value):
    def __str__(self):
        return f'"{self.value}"'


class Bool(Value):
    def __str__(self):
        return 'true' if self.value else 'false'


class Application(LispASTNode):
    def __init__(self, function_name, values):
        self.function_name = function_name
        self.values = values

    def __str__(self):
        return f'({self.function_name} {" ".join([str(v) for v in self.values])})'


class ListNode(LispASTNode):
    def __init__(self, items):
        self.items = items

    def __str__(self):
        return f'({" ".join([str(i) for i in self.items])})'


class FunctionDefinition(LispASTNode):
    pass
