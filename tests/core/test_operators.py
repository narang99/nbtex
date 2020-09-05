import unittest

from nbtex.core.operators import (
    InvertibleInfixOperator,
    InvertibleOperator,
    BasicOperator,
)


def _push_combine(string):
    return string + "1"


def _pop_combine(string):
    return string[:-1] if len(string) > 0 else string


class TestCoreOperators(unittest.TestCase):
    def test_basic_operator(self):
        basic_operator = BasicOperator(0, _push_combine)
        output = basic_operator("x2")
        self.assertEqual(output, "x21")

    def test_invertible_operator(self):
        invertible_operator = InvertibleOperator(0, _push_combine, _pop_combine)
        after_combine = invertible_operator("x")
        self.assertEqual(after_combine, "x1")
        after_inv_combine = (~invertible_operator)(after_combine)
        self.assertEqual(after_inv_combine, "x")

    def test_invertible_operator_without_invert(self):
        invertible_operator = InvertibleOperator(0, _push_combine)
        after_combine = invertible_operator("x")
        after_inv_combine = (~invertible_operator)("x")
        self.assertEqual(after_combine, "x1")
        self.assertEqual(after_inv_combine, "x1")

    def test_precedence(self):
        operator = BasicOperator(0, _push_combine)
        invertible_operator = InvertibleOperator(0, _push_combine)
        invertible_infix_operator = InvertibleInfixOperator(0, "+")
        self.assertEqual(operator.precedence, 0)
        self.assertEqual(invertible_operator.precedence, 0)
        self.assertEqual(invertible_infix_operator.precedence, 0)

    def test_invertible_infix_operator(self):
        operator = InvertibleInfixOperator(0, "+", "-")
        after_combine = operator("1", "2")
        after_invert_combine = (~operator)("1", "2")
        self.assertEqual(after_combine, "1 + 2")
        self.assertEqual(after_invert_combine, "1 - 2")

    def test_inveritble_infix_without_invert(self):
        operator = InvertibleInfixOperator(0, "+")
        after_combine = operator("1", "2")
        after_invert_combine = (~operator)("1", "2")
        self.assertEqual(after_combine, "1 + 2")
        self.assertEqual(after_invert_combine, "1 + 2")


if __name__ == "__main__":
    unittest.main()
