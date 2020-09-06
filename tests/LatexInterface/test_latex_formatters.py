import unittest
from nbtex.LatexInterface.LatexFormatters import LatexBasicFormatter, LatexSeriesFormatter, LatexDerivativesFormatter


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

class TestLatexSeriesFormatter(unittest.TestCase):
    def test_summation(self):
        summation_just_wrt = LatexSeriesFormatter.summation('x+1', 'x')
        summation_wrt_lower = LatexSeriesFormatter.summation('x+1', 'x', '1')
        summation_wrt_lower_upper = LatexSeriesFormatter.summation('x+1', 'x', '1', '10')
        self.assertEqual(summation_just_wrt, r'\sum_{x} {x+1}') 
        self.assertEqual(summation_wrt_lower, r'\sum_{x=1} {x+1}')
        self.assertEqual(summation_wrt_lower_upper, r'\sum_{x=1}^{10} {x+1}')

    def test_product(self):
        product_just_wrt = LatexSeriesFormatter.product('x+1', 'x')
        product_wrt_lower = LatexSeriesFormatter.product('x+1', 'x', '1')
        product_wrt_lower_upper = LatexSeriesFormatter.product('x+1', 'x', '1', '10')
        self.assertEqual(product_just_wrt, r'\prod_{x} {x+1}') 
        self.assertEqual(product_wrt_lower, r'\prod_{x=1} {x+1}')
        self.assertEqual(product_wrt_lower_upper, r'\prod_{x=1}^{10} {x+1}')
    
    def test_integral(self):
        int_just_wrt = LatexSeriesFormatter.integral('x+1', 'x')
        int_wrt_lower = LatexSeriesFormatter.integral('x+1', 'x', '1')
        int_wrt_lower_upper = LatexSeriesFormatter.integral('x+1', 'x', '1', '10')
        self.assertEqual(int_just_wrt, r'\int {x+1} \hspace{1mm} {dx}') 
        self.assertEqual(int_wrt_lower, r'\int_{1} {x+1} \hspace{1mm} {dx}')
        self.assertEqual(int_wrt_lower_upper, r'\int_{1}^{10} {x+1} \hspace{1mm} {dx}')

    def test_partial_integral(self):
        partial_just_wrt = LatexSeriesFormatter.partial_integral('x+1', 'x')
        partial_wrt_lower = LatexSeriesFormatter.partial_integral('x+1', 'x', '1')
        partial_wrt_lower_upper = LatexSeriesFormatter.partial_integral('x+1', 'x', '1', '10')
        self.assertEqual(partial_just_wrt, r'\int {x+1} \hspace{1mm} {\partial x}') 
        self.assertEqual(partial_wrt_lower, r'\int_{1} {x+1} \hspace{1mm} {\partial x}')
        self.assertEqual(partial_wrt_lower_upper, r'\int_{1}^{10} {x+1} \hspace{1mm} {\partial x}')

class TestLatexDerivativesFormatter(unittest.TestCase):
    def test_partial(self):
        partial = LatexDerivativesFormatter.partial('x')
        self.assertEqual(LatexBasicFormatter.fraction(r'\partial', r'\partial x'), partial)

    def test_partial_of_one_word(self):
        partial_of_one_word = LatexDerivativesFormatter.partial_of('xy', 'x')
        partial_of_one_word_power = LatexDerivativesFormatter.partial_of('x^y', 'x')
        partial_of_one_word_subscript = LatexDerivativesFormatter.partial_of('x_y','x')
        partial_of_one_word_power_subscript = LatexDerivativesFormatter.partial_of('x_y^z', 'x')
        self.assertEqual(partial_of_one_word, LatexBasicFormatter.fraction(r'\partial xy', r'\partial x'))
        self.assertEqual(partial_of_one_word_power, LatexBasicFormatter.fraction(r'\partial x^y', r'\partial x'))
        self.assertEqual(partial_of_one_word_subscript, LatexBasicFormatter.fraction(r'\partial x_y', r'\partial x'))
        self.assertEqual(partial_of_one_word_power_subscript, LatexBasicFormatter.fraction(r'\partial x_y^z', r'\partial x'))
    
    def test_partial_of_multi_word(self):
        partial = LatexDerivativesFormatter.partial_of('x+1', 'x')
        par = LatexDerivativesFormatter.partial('x')
        self.assertEqual(partial, par + r' \left(x+1\right)')

    def test_derivative(self):
        derivative = LatexDerivativesFormatter.derivative('x')
        self.assertEqual(LatexBasicFormatter.fraction(r'd', r'dx'), derivative)

    def test_derivative_of_one_word(self):
        derivative_of_one_word = LatexDerivativesFormatter.derivative_of('xy', 'x')
        derivative_of_one_word_power = LatexDerivativesFormatter.derivative_of('x^y', 'x')
        derivative_of_one_word_subscript = LatexDerivativesFormatter.derivative_of('x_y','x')
        derivative_of_one_word_power_subscript = LatexDerivativesFormatter.derivative_of('x_y^z', 'x')
        self.assertEqual(derivative_of_one_word, LatexBasicFormatter.fraction(r'dxy', r'dx'))
        self.assertEqual(derivative_of_one_word_power, LatexBasicFormatter.fraction(r'dx^y', r'dx'))
        self.assertEqual(derivative_of_one_word_subscript, LatexBasicFormatter.fraction(r'dx_y', r'dx'))
        self.assertEqual(derivative_of_one_word_power_subscript, LatexBasicFormatter.fraction(r'dx_y^z', r'dx'))
    
    def test_derivative_of_multi_word(self):
        derivative = LatexDerivativesFormatter.derivative_of('x+1', 'x')
        der = LatexDerivativesFormatter.derivative('x')
        self.assertEqual(derivative, der + r' \left(x+1\right)')




    
if __name__ == "__main__":
    unittest.main()
