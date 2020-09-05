from nbtex.LatexInterface.LatexFormatters import LatexBasicFormatter
from nbtex.core.operators import InvertibleOperator
from nbtex.core.Precedence import PRECEDENCE

f_combine = LatexBasicFormatter.function_definition
inv_f_combine = LatexBasicFormatter.inverse_function_definition

FunctionCall = InvertibleOperator(PRECEDENCE.POWER, f_combine, inv_f_combine)
