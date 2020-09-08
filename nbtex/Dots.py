from nbtex.core.Ast import Var


class Dots(Var):
    def __init__(self, direc="h"):
        super().__init__(direc + "dots")
        self.direc = direc

    def build(self):
        return (
            r"\cdots"
            if (self.direc == "h" or self.direc == "c")
            else r"\vdots"
            if (self.direc == "v")
            else r"\ddots"
        )

    def clone(self):
        return Dots(self.direc)