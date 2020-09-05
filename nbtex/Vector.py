from nbtex.core.Ast import Var
from nbtex.helpers import varArgFunc


class Vector(Var):
    def __init__(self, name):
        super().__init__(r"\vec{\mathbf{" + name + "}}")


def makeVector(*args):
    return varArgFunc(
        lambda arg: arg if isinstance(arg, Vector) else Vector(str(arg)), *args
    )
