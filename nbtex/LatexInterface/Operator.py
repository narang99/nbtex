class OperatorSymbols:
    def __init__(self):
        pass

    @property
    def plus(self):
        return "+"

    @property
    def minus(self):
        return "-"

    @property
    def multiply(self):
        return "*"

    @property
    def power(self):
        return "^"
    
    @property
    def newline(self):
        return "\\\\"

    @property
    def space(self):
        return "\\hspace{1mm}"

    @property
    def eq(self):
        return "="

    @property
    def lt(self):
        return "<"

    @property
    def leq(self):
        return r"\leq"

    @property
    def gt(self):
        return ">"

    @property
    def geq(self):
        return r"\geq"

    @property
    def nless(self):
        return r"\nless"

    @property
    def nleq(self):
        return r"\nleq"

    @property
    def ngtr(self):
        return r"\ngtr"

    @property
    def ngeq(self):
        return r"\ngeq"

    @property
    def neq(self):
        return r"\neq"


Operator = OperatorSymbols()
