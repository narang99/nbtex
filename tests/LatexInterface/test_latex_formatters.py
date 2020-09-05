import unittest
from nbtex.LatexInterface.LatexFormatters import LatexBasicFormatter


class TextLatexBasicFormatter(unittest.TestCase):
    def test_bold_italics_underline(self):
        bold_string = LatexBasicFormatter.bold("1")
        italics_string = LatexBasicFormatter.italics("1")
        underline_string = LatexBasicFormatter.underline("1")
        self.assertEqual(bold_string, r"\textbf{1}")
        self.assertEqual(italics_string, r"\textit{1}")
        self.assertEqual(underline_string, r"\underline{1}")

    def test_binary_operation_output(self):
        output = LatexBasicFormatter.binary_operation_output("+", "1", "2")
        self.assertEqual(output, "1 + 2")

    def test_surround_with_parens(self):
        output = LatexBasicFormatter.surround_with_parens("1")
        self.assertEqual(output, r"\left(1\right)")


if __name__ == "__main__":
    unittest.main()
