from nbtex.core.operators.Operator import InvertibleOperator
from nbtex.core.Precedence import PRECEDENCE
from nbtex.LatexInterface.LatexFormatters import LatexBasicFormatter


def make_subscript(base, subs):
    return base + LatexBasicFormatter.subscript(subs)


Subscript = InvertibleOperator(PRECEDENCE.POWER, make_subscript)
Bold = InvertibleOperator(PRECEDENCE.POWER, LatexBasicFormatter.bold)
Italics = InvertibleOperator(PRECEDENCE.POWER, LatexBasicFormatter.italics)
Underline = InvertibleOperator(PRECEDENCE.POWER, LatexBasicFormatter.underline)
