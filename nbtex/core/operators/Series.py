from nbtex.core.operators.Operator import InvertibleOperator
from nbtex.LatexInterface.LatexFormatters import LatexSeriesFormatter
from nbtex.core.Precedence import PRECEDENCE

Summation = InvertibleOperator(PRECEDENCE.POWER, LatexSeriesFormatter.summation)

Product = InvertibleOperator(PRECEDENCE.POWER, LatexSeriesFormatter.product)
