import unittest
from nbtex.LatexInterface.LatexFormatters import LatexMatrixFormatter


class TestLatexMatrixFormatter(unittest.TestCase):
    def test_matrix_to_latex(self):
        mtx = [["1", "2", "3"], ["4", "5", "6"]]
        ltx_mtx = LatexMatrixFormatter.matrix_to_latex(mtx)
        self.assertEqual(ltx_mtx, r" 1 &  2 &  3 \\ 4 &  5 &  6 ")

    def test_empty_power_subscript(self):
        emppow = LatexMatrixFormatter.empty_power()
        empsub = LatexMatrixFormatter.empty_subscript()
        subscript = LatexMatrixFormatter.subscript_of_matrix('1')
        power = LatexMatrixFormatter.power_of_matrix('1')
        self.assertEqual(emppow, "")
        self.assertEqual(empsub, "")
        self.assertEqual(subscript, r"_{1}")
        self.assertEqual(power, r"^{1}")

    def test_create_env(self):
        beginb, endb = LatexMatrixFormatter.create_env("[]")
        beginp, endp = LatexMatrixFormatter.create_env("()")
        beginv, endv = LatexMatrixFormatter.create_env("||")
        beginV, endV = LatexMatrixFormatter.create_env("||||")
        begin, end = LatexMatrixFormatter.create_env("else")

        self.assertEqual(beginb, r"\begin{bmatrix}")
        self.assertEqual(endb, r"\end{bmatrix}")
        self.assertEqual(beginp, r"\begin{pmatrix}")
        self.assertEqual(endp, r"\end{pmatrix}")
        self.assertEqual(beginv, r"\begin{vmatrix}")
        self.assertEqual(endv, r"\end{vmatrix}")
        self.assertEqual(beginV, r"\begin{Vmatrix}")
        self.assertEqual(endV, r"\end{Vmatrix}")
        self.assertEqual(begin, r"\begin{matrix}")
        self.assertEqual(end, r"\end{matrix}")

