import nbtex.core.operators as Operator
from nbtex.helpers import varArgFunc
from nbtex.core.Precedence import PRECEDENCE
from nbtex.LatexInterface import LatexBasicFormatter
from nbtex.platforms.jupyter import latex


class Var:
    def __init__(self, name, backward_operation=None):
        self._name, self._backward_operation = name, backward_operation

    def clone(self):
        if self.backward_operation is None:
            return Var(self._name)
        return Var(self._name, self._backward_operation.clone())

    def __str__(self):
        return self.build()

    def __repr__(self):
        return self.__str__()

    @property
    def backward_operation(self):
        return self._backward_operation

    @property
    def precedence(self):
        return (
            PRECEDENCE.VAR
            if self._backward_operation is None
            else self._backward_operation.precedence
        )

    def build(self):
        return (
            self._name
            if self._backward_operation is None
            else self._backward_operation.build()
        )

    @staticmethod
    def operation(operator, *args):
        operation = Operation(operator)
        args = makeVar(*args)
        if isinstance(args, list):
            output = Var("output", operation(*args))
        else:
            output = Var("output", operation(args))
        return output

    def __invert__(self):
        if self._backward_operation is not None:
            self._backward_operation = self._backward_operation.__invert__()
        return self

    def __call__(self, *args):
        return Var.operation(Operator.FunctionCall, self, *args)

    def __add__(self, other):
        return Var.operation(Operator.Plus, self, other)

    def __sub__(self, other):
        return Var.operation(Operator.Minus, self, other)

    def __mul__(self, other):
        return Var.operation(Operator.Multiply, self, other)

    def __pow__(self, other):
        return Var.operation(Operator.Power, self, other)

    def __or__(self, other):
        return Var.operation(Operator.Space, self, other)

    def __and__(self, other):
        return Var.operation(Operator.Newline, self, other)

    def __lt__(self, other):
        return Var.operation(Operator.LessThan, self, other)

    def __gt__(self, other):
        return Var.operation(Operator.GreaterThan, self, other)

    def __le__(self, other):
        return Var.operation(Operator.LessThanEqual, self, other)

    def __ge__(self, other):
        return Var.operation(Operator.GreaterThanEqual, self, other)

    def __neg__(self):
        return Var.operation(Operator.Negate, self)

    def __truediv__(self, other):
        return Var.operation(Operator.Fraction, self, other)

    def equals(self, other):
        return Var.operation(Operator.Equal, self, other)

    def not_equals(self, other):
        return Var.operation(~Operator.Equal, self, other)

    def root(self, power):
        return Var.operation(Operator.Root, self, power)

    def sum_over(self, wrt="", lower="", upper=""):
        return Var.operation(Operator.Summation, self, wrt, lower, upper)

    def product_over(self, wrt="", lower="", upper=""):
        return Var.operation(Operator.Product, self, wrt, lower, upper)

    def integral_over(self, wrt="", lower="", upper=""):
        return Var.operation(Operator.Integral, self, wrt, lower, upper)

    def differentiate(self, wrt):
        return Var.operation(Operator.Derivative, self, wrt)

    def partial_integral_over(self, wrt="", lower="", upper=""):
        return Var.operation(Operator.PartialIntegral, self, wrt, lower, upper)

    def partial_differentiate(self, wrt):
        return Var.operation(Operator.PartialDerivative, self, wrt)

    def subscript(self, subs):
        return Var.operation(Operator.Subscript, self, subs)

    def bold(self):
        return self.use_operator_on_leaf(Operator.Bold)

    def italics(self):
        return self.use_operator_on_leaf(Operator.Italics)

    def underline(self):
        return self.use_operator_on_leaf(Operator.Underline)

    def use_operator_on_leaf(self, operator):
        if self.backward_operation is None:
            return Var.operation(operator, self)
        else:
            self._backward_operation = self.backward_operation.use_operator_on_leaf(
                operator
            )
            return self


def isVar(a):
    return isinstance(a, Var)


def makeVar(*args):
    return varArgFunc(lambda arg: arg.clone() if isVar(arg) else Var(str(arg)), *args)


def addEnv(s, env="gather*"):
    env = "{" + env + "}"
    return r"\begin" + env + str(s) + r"\end" + env


class Operation:
    def __init__(self, operator):
        self._operator = operator
        self._args = None

    def clone(self):
        return self
        # NOTE: Deep Clone: This is a costly operation
        #       Shallow cloning done for now
        # cloned_op = Operation(self._operator)
        # if self._args is None: return cloned_op
        # return cloned_op(*self._args)

    @property
    def precedence(self):
        return self._operator.precedence

    def __call__(self, *args):
        self._args = args
        return self

    def use_operator_on_leaf(self, operator):
        args = [arg.use_operator_on_leaf(operator) for arg in self._args]
        self._args = args
        return self

    def _is_invertible(self, op):
        return isinstance(op, Operator.InvertibleOperator)

    def build(self):
        args = [self._build_and_surround(makeVar(arg)) for arg in self._args]
        return self._operator(*args)

    def _build_and_surround(self, var_instance):
        return (
            self._get_surrounded_with_parens(var_instance.build())
            if self._should_surround_with_parens(var_instance)
            else var_instance.build()
        )

    def _get_surrounded_with_parens(self, string):
        return LatexBasicFormatter.surround_with_parens(string)

    def _should_surround_with_parens(self, var_instance):
        return (
            var_instance.backward_operation is not None
            and var_instance.backward_operation.precedence < self.precedence
        )

    def __invert__(self):
        if self._is_invertible(self._operator):
            self._operator = ~self._operator
        return self
