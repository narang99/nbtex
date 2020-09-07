import unittest
from nbtex.LatexInterface.LatexFormatters import LatexBasicFormatter

class TestLatexBasicFormatter(unittest.TestCase):
    def test_bold_italics_underline(self):
        bold_string = LatexBasicFormatter.bold("1")
        italics_string = LatexBasicFormatter.italics("1")
        underline_string = LatexBasicFormatter.underline("1")
        self.assertEqual(bold_string, r"\textbf{1}")
        self.assertEqual(italics_string, r"\textit{1}")
        self.assertEqual(underline_string, r"\underline{1}")

    def test_binary_operation_output(self):
        add_output = LatexBasicFormatter.binary_operation_output("+", "1", "2")
        sub_output = LatexBasicFormatter.binary_operation_output("-", "1", "2")
        self.assertEqual(add_output, "1 + 2")
        self.assertEqual(sub_output, '1 - 2')

    def test_surround_with_parens(self):
        output = LatexBasicFormatter.surround_with_parens("1")
        self.assertEqual(output, r"\left(1\right)")

    def test_negate_unnegate(self):
        negative = LatexBasicFormatter.negate('123')
        still_negative = LatexBasicFormatter.negate('-123')
        positive = LatexBasicFormatter.unnegate('-123')
        still_positive = LatexBasicFormatter.unnegate('123')
        self.assertEqual(negative, '-123')
        self.assertEqual(still_negative, '-123')
        self.assertEqual(positive, '123')
        self.assertEqual(still_positive, '123')

    def test_fraction(self):
        fraction = LatexBasicFormatter.fraction('1', '2')
        self.assertEqual(fraction, r'\frac{1}{2}')
    
    def test_subscript_superscript(self):
        subscript = LatexBasicFormatter.subscript('1')
        superscript = LatexBasicFormatter.superscript('1')
        self.assertEqual(subscript, '_1')
        self.assertEqual(superscript, '^1')

    def test_root(self):
        nthRoot = LatexBasicFormatter.root('1', 'n')
        self.assertEqual(nthRoot, r'\sqrt[\leftroot{-1}\uproot{1}n]{1}')

    def test_function_def(self):
        noarg = LatexBasicFormatter.function_definition('g')
        monoarg = LatexBasicFormatter.function_definition('g', 'x')
        twoArg = LatexBasicFormatter.function_definition('g', 'x', 'y')
        self.assertEqual(noarg, 'g()')
        self.assertEqual(monoarg, 'g(x)')
        self.assertEqual(twoArg, 'g(x, y)')

    def test_inverse_function_def(self):
        noarg = LatexBasicFormatter.inverse_function_definition('g')
        monoarg = LatexBasicFormatter.inverse_function_definition('g', 'x')
        twoArg = LatexBasicFormatter.inverse_function_definition('g', 'x', 'y')
        self.assertEqual(noarg, 'g^{-1}()')
        self.assertEqual(monoarg, 'g^{-1}(x)')
        self.assertEqual(twoArg, 'g^{-1}(x, y)')