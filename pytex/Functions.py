
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/Functions.ipynb
from pytex.Variables import *
from pytex.helpers import varArgFunc

class Sum(Var):
    def __init__(self, func, it='i', lower=None, upper=None):
        super().__init__('summation')
        self.it = makeVar(it)
        self.f = makeVar(func)
        self.lower, self.upper = lower, upper
    # non callable
    def __call__(self):
        raise Exception('summation is non callable')
    def build(self):
        lower = ''
        if self.lower is not None:
            l = makeVar(self.lower)
            lower = r"_{" + self.it.build() + "=" + l.build() + "}"
        else:
            lower = r"_{" + self.it.build() + "}"
        upper = ''
        if self.upper is not None:
            u = makeVar(self.upper)
            upper = r"^" + r"{" + u.build() + "}"
        else: upper = ''
        return r"\sum" + lower + upper + ' ' + self.f.build()

class Partial(Var):
    def __init__(self, wrt, degree=1):
        super().__init__('partial')
        self.degree, self.wrt = makeVar(degree, wrt)
    def __str__(self):
        return f"partial wrt {self.wrt.build()} degree {self.degree.build()}"
    def build(self):
        deg = ('^{' + self.degree.build()) + '}' if self.degree.build() != '1' else ''
        return r"\frac{\partial" + deg + "}{\partial" + deg + r" " + self.wrt.build() + r"}"
#         return r"\frac{\partial" + deg + "}{\partial" + deg + r" \left(" + self.wrt.build() + r"\right)}"

def makePartials(*args):
    return varArgFunc(lambda arg: Partial(*arg) if not isinstance(arg, Partial) else arg, *args)

class Derivative(Var):
    def __init__(self, wrt, degree=1):
        super().__init__(wrt)
        self.degree = makeVar(degree)
    def build(self):
        deg = ('^{' + makeVar(self.degree).build()) + '}' if self.degree != 1 else ''
        return r"\frac{d" + deg + "}{d" + deg + " " + self.name + "}"

def makeDerivatives(*args):
    return varArgFunc(lambda arg: (Derivative(*arg) if not isinstance(arg, Derivative)
                                   else arg), *args)