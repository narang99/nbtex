class LatexBasicFormatter:
    def __init__(self):
        pass

    @staticmethod
    def bold(string):
        return "\\textbf{" + string + "}"

    @staticmethod
    def italics(string):
        return "\\textit{" + string + "}"

    @staticmethod
    def underline(string):
        return "\\underline{" + string + "}"

    @staticmethod
    def binary_operation_output(binary_operator, a1, a2):
        return f"{a1} {binary_operator} {a2}"

    @staticmethod
    def surround_with_parens(string):
        return f"\\left({string}\\right)"

    @staticmethod
    def negate(string):
        if string[0] == "-":
            return string
        else:
            return f"-{string}"

    @staticmethod
    def unnegate(string):
        return string[1:] if (string[0] == "-") else string

    @staticmethod
    def fraction(num, den):
        num, den = LatexBasicFormatter.surround_all_with_braces(num, den)
        return f"\\frac{num}{den}"

    @staticmethod
    def subscript(string):
        return f"_{string}"

    @staticmethod
    def superscript(string):
        return f"^{string}"

    @staticmethod
    def surround_with_braces(string):
        return "{" + string + "}"

    @staticmethod
    def surround_all_with_braces(*args):
        if len(args) == 1:
            return LatexBasicFormatter.surround_with_braces(args[0])
        else:
            return [LatexBasicFormatter.surround_with_braces(arg) for arg in args]

    @staticmethod
    def root(num, nth):
        return r"\sqrt[\leftroot{-1}\uproot{1}" + nth + r"]{" + num + r"}"

    @staticmethod
    def function_definition(f, *args):
        if len(args) == 0:
            return f"{f}()"
        s = ""
        for arg in args:
            s += f"{arg}, "
        s = s[:-2]
        return f"{f}({s})"

    @staticmethod
    def inverse_function_definition(f, *args):
        _1 = LatexBasicFormatter.surround_with_braces("-1")
        return LatexBasicFormatter.function_definition(f"{f}^{_1}", *args)
