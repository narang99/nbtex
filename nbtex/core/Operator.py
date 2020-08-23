
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/Operator.ipynb
from nbtex.core.Precedence import PRECEDENCE
from nbtex.LatexInterface.LatexFormatters import LatexBasicFormatter
from nbtex.LatexInterface import Operator
from functools import partial
from nbtex.LatexInterface.LatexFormatters import LatexSeriesFormatter, LatexDerivativesFormatter

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
            return InvertibleOperator(self.precedence, self._invert_combine, self._combine)
        else:
            return self

def _infix_combine(op):
    return partial(LatexBasicFormatter.binary_operation_output, op)

class InvertibleInfixOperator(InvertibleOperator):
    def __init__(self, precedence, op, invert_op=None):
        c, invc = _infix_combine(op), _infix_combine(invert_op)
        if invert_op is None:
            super().__init__(precedence, c)
        else:
            super().__init__(precedence, c, invc)

Plus = InvertibleInfixOperator(PRECEDENCE.ARITHMATIC_ADD, Operator.plus)
Minus = InvertibleInfixOperator(PRECEDENCE.ARITHMATIC_ADD, Operator.minus)
Equal = InvertibleInfixOperator(PRECEDENCE.EQUALITY, Operator.eq, Operator.neq)
LessThan = InvertibleInfixOperator(PRECEDENCE.COMPARE, Operator.lt, Operator.nless)
LessThanEqual = InvertibleInfixOperator(PRECEDENCE.COMPARE, Operator.leq, Operator.nleq)
GreaterThan = InvertibleInfixOperator(PRECEDENCE.COMPARE, Operator.gt, Operator.ngtr)
GreaterThanEqual = InvertibleInfixOperator(PRECEDENCE.COMPARE, Operator.geq, Operator.ngeq)
Space = InvertibleInfixOperator(PRECEDENCE.EQUALITY, Operator.space)

Negate = InvertibleOperator(PRECEDENCE.POWER,
                            LatexBasicFormatter.negate,
                            LatexBasicFormatter.unnegate)

mult_combine = _infix_combine(Operator.multiply)
frac_combine = LatexBasicFormatter.fraction

Multiply = InvertibleOperator(PRECEDENCE.ARITHMATIC_MULT, mult_combine, frac_combine)
Fraction = ~Multiply

power_combine = _infix_combine(Operator.power)

Power = InvertibleOperator(PRECEDENCE.POWER, power_combine, LatexBasicFormatter.root)
Root = ~Power

f_combine = LatexBasicFormatter.function_definition
inv_f_combine = LatexBasicFormatter.inverse_function_definition

FunctionCall = InvertibleOperator(PRECEDENCE.POWER, f_combine, inv_f_combine)

Summation = InvertibleOperator(PRECEDENCE.POWER,
                               LatexSeriesFormatter.summation)

Product = InvertibleOperator(PRECEDENCE.POWER,
                             LatexSeriesFormatter.product)

def inv_integral(function, wrt, lower='', upper=''):
    return LatexDerivativesFormatter.derivative_of(function, wrt)

Integral =  InvertibleOperator(PRECEDENCE.POWER,
                               LatexSeriesFormatter.integral,
                               inv_integral)
Derivative = ~Integral

def inv_partial(function, wrt, lower='', upper=''):
    return LatexDerivativesFormatter.partial_of(function, wrt)

PartialIntegral = InvertibleOperator(PRECEDENCE.POWER,
                                     LatexSeriesFormatter.partial_integral,
                                     inv_partial)
PartialDerivative = ~PartialIntegral