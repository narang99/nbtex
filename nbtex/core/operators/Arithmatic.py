from nbtex.core.operators.Operator import (
    BasicOperator,
    InvertibleInfixOperator,
    InvertibleOperator,
    infix_combine,
)
from nbtex.core.Precedence import PRECEDENCE
from nbtex.LatexInterface import Operator, LatexBasicFormatter

Plus = InvertibleInfixOperator(PRECEDENCE.ARITHMATIC_ADD, Operator.plus, Operator.minus)
Minus = ~Plus
Equal = InvertibleInfixOperator(PRECEDENCE.EQUALITY, Operator.eq, Operator.neq)
LessThan = InvertibleInfixOperator(PRECEDENCE.COMPARE, Operator.lt, Operator.nless)
LessThanEqual = InvertibleInfixOperator(PRECEDENCE.COMPARE, Operator.leq, Operator.nleq)
GreaterThan = InvertibleInfixOperator(PRECEDENCE.COMPARE, Operator.gt, Operator.ngtr)
GreaterThanEqual = InvertibleInfixOperator(
    PRECEDENCE.COMPARE, Operator.geq, Operator.ngeq
)
Space = InvertibleInfixOperator(PRECEDENCE.EQUALITY, Operator.space)
Newline = InvertibleInfixOperator(PRECEDENCE.EQUALITY, Operator.newline)

Negate = InvertibleOperator(
    PRECEDENCE.POWER, LatexBasicFormatter.negate, LatexBasicFormatter.unnegate
)

mult_combine = infix_combine(Operator.multiply)
frac_combine = LatexBasicFormatter.fraction

Multiply = InvertibleOperator(PRECEDENCE.ARITHMATIC_MULT, mult_combine, frac_combine)
Fraction = ~Multiply

power_combine = infix_combine(Operator.power)

Power = InvertibleOperator(PRECEDENCE.POWER, power_combine, LatexBasicFormatter.root)
Root = ~Power
