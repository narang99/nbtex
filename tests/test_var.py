import unittest
from pytex import Var, makeVar

class TestVar(unittest.TestCase):
    def test_makeVar(self):
        a = makeVar('a')
        b = makeVar(a)
        self.assertTrue(isinstance(a, Var),
                        'makeVar not returning Var on passing string')
        self.assertTrue(isinstance(b, Var),
                        'makeVar not returning Var on passing Var type')
        
if(__name__=='__main__'):
  unittest.main()