from nbtex.core.operators.Operator import InvertibleOperator
from nbtex.LatexInterface.LatexFormatters import (
    LatexSeriesFormatter,
    LatexDerivativesFormatter,
)
from nbtex.core.Precedence import PRECEDENCE


def inv_integral(function, wrt, lower="", upper=""):
    return LatexDerivativesFormatter.derivative_of(function, wrt)


Integral = InvertibleOperator(
    PRECEDENCE.POWER, LatexSeriesFormatter.integral, inv_integral
)
Derivative = ~Integral


def inv_partial(function, wrt, lower="", upper=""):
    return LatexDerivativesFormatter.partial_of(function, wrt)


PartialIntegral = InvertibleOperator(
    PRECEDENCE.POWER, LatexSeriesFormatter.partial_integral, inv_partial
)
PartialDerivative = ~PartialIntegral
