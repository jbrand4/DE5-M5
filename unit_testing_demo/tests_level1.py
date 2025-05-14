import unittest
from calculator_app import Calculator

class TestOperations(unittest.TestCase):

    def test_sum(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.do_sum(), 10, 'The sum is wrong (not 10).')

    #test difference
    def test_diff(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.do_subtract(), 6, 'The difference is wrong (not 6).')
    
    #test product
    def test_prod(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.do_product(), 16, 'The produt is wrong (not 16).')

    #test quotient
    def test_quot(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.do_divide(), 4, 'The quotient is wrong (not 4).')

if __name__ == '__main__':
    unittest.main()