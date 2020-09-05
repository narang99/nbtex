from nbtex.LatexInterface.LatexFormatters import LatexBasicFormatter


class LatexDerivativesFormatter:
    @staticmethod
    def is_one_word(expr):
        for w in expr:
            if not w.isalnum() and w != "_" and w != "^":
                return False
        return True

    @staticmethod
    def partial(wrt):
        return LatexBasicFormatter.fraction("\\partial", f"\\partial {wrt}")

    @staticmethod
    def partial_of(function, wrt):
        if not LatexDerivativesFormatter.is_one_word(function):
            function = LatexBasicFormatter.surround_with_parens(function)
            par = LatexDerivativesFormatter.partial(wrt)
            return f"{par} {function}"
        return LatexBasicFormatter.fraction(f"\\partial {function}", f"\\partial {wrt}")

    @staticmethod
    def derivative(wrt):
        return LatexBasicFormatter.fraction("d", f"d{wrt}")

    @staticmethod
    def derivative_of(function, wrt):
        if not LatexDerivativesFormatter.is_one_word(function):
            function = LatexBasicFormatter.surround_with_parens(function)
            der = LatexDerivativesFormatter.derivative(wrt)
            return f"{der} {function}"
        return LatexBasicFormatter.fraction(f"d{function}", f"d{wrt}")
