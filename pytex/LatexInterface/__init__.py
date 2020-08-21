from pytex.LatexInterface.Arrow import Arrow
from pytex.LatexInterface.Operator import Operator
from pytex.LatexInterface.Set import Set

def create_latex_for_binary_operator(binary_operator, a1, a2):
    return f'{a1} {binary_operator.latex} {a2}'

def surround_with_parens(string):
    return f'({string})'
