class PrecedenceValues:
    def __init__(self):
        pass

    @property
    def POWER(self):
        return 13

    @property
    def VAR(self):
        return self.POWER

    @property
    def UNARY(self):
        return 12

    @property
    def ARITHMATIC_MULT(self):
        return 11

    @property
    def ARITHMATIC_ADD(self):
        return 10

    @property
    def SHIFT(self):
        return 9

    @property
    def UNARY_AND(self):
        return 8

    @property
    def UNARY_OR_XOR(self):
        return 7

    @property
    def COMPARE(self):
        return 6

    @property
    def EQUALITY(self):
        return 5


PRECEDENCE = PrecedenceValues()
