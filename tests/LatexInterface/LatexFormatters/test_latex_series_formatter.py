import unittest
from nbtex.LatexInterface.LatexFormatters import LatexSeriesFormatter

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