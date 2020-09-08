import unittest
import nbtex.core.operators.Arithmatic as A
import nbtex.core.operators.Derivative as D
import nbtex.core.operators.FunctionCall as F
import nbtex.core.operators.Series as S
import nbtex.core.operators.UnaryFormatting as U

# TODO: Writing tests for Derivative, FunctionCall, Series, UnaryFormatting
class TestArithmaticOperators(unittest.TestCase):
    def test_add_minus(self):
        plus = A.Plus("1", "2")
        minus = A.Minus("1", "2")
        self.assertEqual(plus, "1 + 2")
        self.assertEqual(minus, "1 - 2")
        self.assertEqual(plus, (~A.Minus)("1", "2"))
        self.assertEqual(minus, (~A.Plus)("1", "2"))

    def test_mult_frac(self):
        mult = A.Multiply("1", "2")
        frac = A.Fraction("1", "2")
        self.assertEqual(mult, "1 * 2")
        self.assertEqual(frac, r"\frac{1}{2}")
        self.assertEqual(mult, (~A.Fraction)("1", "2"))
        self.assertEqual(frac, (~A.Multiply)("1", "2"))

    def test_power_root(self):
        power = A.Power('1','2')
        root = A.Root('1', '2')
        self.assertEqual(power, '1 ^ 2')
        self.assertEqual(root, r'\sqrt[\leftroot{-1}\uproot{1}2]{1}')
        self.assertEqual(power, (~A.Root)('1','2'))
        self.assertEqual(root, (~A.Power)('1', '2'))

    def test_negate(self):
        negated = A.Negate('1')
        still_negated = A.Negate('-1')
        unnegated = (~A.Negate)('-1')
        still_unnegated = (~A.Negate)('1')
        self.assertEqual(negated, '-1')
        self.assertEqual(unnegated, '1')
        self.assertEqual(still_negated, '-1')
        self.assertEqual(still_unnegated, '1')

    def test_space(self):
        space = A.Space('1', '2')
        self.assertEqual(space, r'1 \hspace{1mm} 2')
    
    def test_compare_operators(self):
        # TODO: All relational operators tests
        pass

