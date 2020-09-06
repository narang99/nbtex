from nbtex.LatexInterface.LatexFormatters.LatexBasicFormatter import LatexBasicFormatter
from nbtex.LatexInterface.Operator import Operator


class LatexSeriesFormatter:
    @staticmethod
    def integral(func, wrt, lower="", upper=""):
        func, wrt, lower, upper = LatexSeriesFormatter._preprocess_args(
            func, f"d{wrt}", lower, upper
        )
        return f"\\int{lower}{upper} {func} {Operator.space} {wrt}"

    @staticmethod
    def partial_integral(func, wrt, lower="", upper=""):
        func, wrt, lower, upper = LatexSeriesFormatter._preprocess_args(
            func, f"\\partial {wrt}", lower, upper
        )
        return f"\\int{lower}{upper} {func} {Operator.space} {wrt}"

    @staticmethod
    def summation(func, wrt="", lower="", upper=""):
        lower = f"{wrt}={lower}" if lower != "" and wrt != "" else wrt
        func, _, lower, upper = LatexSeriesFormatter._preprocess_args(
            func, wrt, lower, upper
        )
        return f"\\sum{lower}{upper} {func}"

    @staticmethod
    def product(func, wrt="", lower="", upper=""):
        lower = f"{wrt}={lower}" if lower != "" and wrt != "" else wrt
        func, _, lower, upper = LatexSeriesFormatter._preprocess_args(
            func, wrt, lower, upper
        )
        return f"\\prod{lower}{upper} {func}"

    @staticmethod
    def _preprocess_args(func, wrt, lower, upper):
        lower, upper = LatexSeriesFormatter._format_lower_upper(lower, upper)
        func, wrt = LatexBasicFormatter.surround_all_with_braces(func, wrt)
        return func, wrt, lower, upper

    @staticmethod
    def _format_lower_upper(lower, upper):
        lower = LatexBasicFormatter.surround_with_braces(lower) if lower != "" else ""
        if lower != "":
            lower = LatexBasicFormatter.subscript(lower)

        upper = LatexBasicFormatter.surround_with_braces(upper) if upper != "" else ""
        if upper != "":
            upper = LatexBasicFormatter.superscript(upper)
        return lower, upper
