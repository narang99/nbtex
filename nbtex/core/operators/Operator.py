from nbtex.LatexInterface.LatexFormatters import LatexBasicFormatter
from functools import partial


class BasicOperator:
    def __init__(self, precedence, combine):
        self._precedence, self._combine = precedence, combine

    def __call__(self, *args):
        return self._combine(*args)

    @property
    def precedence(self):
        return self._precedence


class InvertibleOperator(BasicOperator):
    def __init__(self, precedence, combine, invert_combine=None):
        super().__init__(precedence, combine)
        self._invert_combine = invert_combine

    def __call__(self, *args):
        return super().__call__(*args)

    def __invert__(self):
        if self._invert_combine is not None:
            return InvertibleOperator(
                self.precedence, self._invert_combine, self._combine
            )
        else:
            return self


def infix_combine(op):
    return partial(LatexBasicFormatter.binary_operation_output, op)


class InvertibleInfixOperator(InvertibleOperator):
    def __init__(self, precedence, op, invert_op=None):
        c, invc = infix_combine(op), infix_combine(invert_op)
        if invert_op is None:
            super().__init__(precedence, c)
        else:
            super().__init__(precedence, c, invc)
