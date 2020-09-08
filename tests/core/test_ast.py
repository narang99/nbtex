import unittest
from nbtex.core.Ast import Var, makeVar
import nbtex.core.operators.Arithmatic as A


class TestAst(unittest.TestCase):
    def test_var_init(self):
        a = Var("a")
        self.assertEqual(a.build(), "a")
        self.assertIsInstance(a, Var)

    def test_pass_single_in_makeVar(self):
        one_var = makeVar("o")
        self.assertIsInstance(one_var, Var)

    def test_pass_multiple_in_makeVar(self):
        a, b, _1 = makeVar("a", "b", 1)
        self.assertIsInstance(a, Var)
        self.assertIsInstance(b, Var)
        self.assertIsInstance(_1, Var)
        lst = makeVar("a", "b")
        self.assertIsInstance(lst, list)

    def test_pass_Var_in_makeVar(self):
        a = makeVar("a")
        na = makeVar(a)
        self.assertEqual(a.build(), na.build())
        self.assertIsNot(a, na)

    def test_basic_aritmatic(self):
        a, b = makeVar("a", "b")
        c = a + b
        self.assertIsNot(c, a)
        self.assertIsNot(c, b)
        self.assertEqual(c.build(), A.Plus("a", "b"))
        c = a - b
        self.assertEqual(c.build(), A.Minus("a", "b"))
        c = a * b
        self.assertEqual(c.build(), A.Multiply("a", "b"))
        c = a / b
        self.assertEqual(c.build(), A.Fraction("a", "b"))
        c = a ** b
        self.assertEqual(c.build(), A.Power("a", "b"))
        c = a.root(b)
        self.assertEqual(c.build(), A.Root('a','b'))

    def test_comparison_operators(self):
        a, b = makeVar("a", "b")
        c = a < b
        self.assertEqual(c.build(), A.LessThan("a", "b"))
        c = a > b
        self.assertEqual(c.build(), A.GreaterThan("a", "b"))
        c = a <= b
        self.assertEqual(c.build(), A.LessThanEqual("a", "b"))
        c = a >= b
        self.assertEqual(c.build(), A.GreaterThanEqual("a", "b"))
        c = a.equals(b)
        self.assertEqual(c.build(), A.Equal("a", "b"))
        c = a.not_equals(b)
        self.assertEqual(c.build(), (~A.Equal)("a", "b"))

    def test_inverted_basic_arithmatic(self):
        a, b = makeVar("a", "b")
        c = a + b
        self.assertIsNot(c, a)
        self.assertIsNot(c, b)
        self.assertEqual((~c).build(), A.Minus("a", "b"))
        c = a - b
        self.assertEqual((~c).build(), A.Plus("a", "b"))
        c = a * b
        self.assertEqual((~c).build(), A.Fraction("a", "b"))
        c = a / b
        self.assertEqual((~c).build(), A.Multiply("a", "b"))
        c = a ** b
        self.assertEqual((~c).build(), A.Root("a", "b"))
        c = a.root(b)
        self.assertEqual((~c).build(), A.Power('a','b'))

    def test_inverted_comparison_operators(self):
        a, b = makeVar("a", "b")
        c = a < b
        self.assertEqual((~c).build(), (~A.LessThan)("a", "b"))
        c = a > b
        self.assertEqual((~c).build(), (~A.GreaterThan)("a", "b"))
        c = a <= b
        self.assertEqual((~c).build(), (~A.LessThanEqual)("a", "b"))
        c = a >= b
        self.assertEqual((~c).build(), (~A.GreaterThanEqual)("a", "b"))
        c = a.equals(b)
        self.assertEqual((~c).build(), (~A.Equal)("a", "b"))

