import unittest
from nbtex.LatexInterface.LatexFormatters import LatexDerivativesFormatter, LatexBasicFormatter

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
