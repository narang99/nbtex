class LatexMatrixFormatter:
    def __init__(self):
        pass

    @staticmethod
    def row_to_latex(row):
        s = ""
        for ele in row:
            s += " " + ele + " & "
        s = s[:-2] + r"\\"
        return s

    @staticmethod
    def matrix_to_latex(matrix):
        s = ""
        for row in matrix:
            s += LatexMatrixFormatter.row_to_latex(row)
        s = s[:-2]
        return s

    @staticmethod
    def create_env(surround):
        env = (
            r"{bmatrix}"
            if surround == "[]"
            else r"{pmatrix}"
            if surround == "()"
            else r"{vmatrix}"
            if surround == "||"
            else r"{Vmatrix}"
            if (surround == "|| ||" or surround == "||||")
            else r"{matrix}"
        )
        begin = r"\begin" + env
        end = r"\end" + env
        return begin, end

    @staticmethod
    def subscript_of_matrix(subscript):
        return "_{" + subscript + "}"

    @staticmethod
    def power_of_matrix(power):
        return "^{" + power + "}"

    @staticmethod
    def empty_power():
        return ""

    @staticmethod
    def empty_subscript():
        return ""
