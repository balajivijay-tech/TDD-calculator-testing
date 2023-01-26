from Calculator import Calculator
import unittest
class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    def test_add(self):
        self.assertEqual(10, self.calc.add(3, 7), "The addition is wrong")
    def test_subtract(self):
        self.assertEqual(12, self.calc.subtract(15, 3), "Subtraction is wrong")
    def test_multiply(self):
        self.assertEqual(30, self.calc.multiply(5, 6), "Multiplication is wrong")
    def test_divide(self):
        self.assertEqual(7, self.calc.divide(63, 9), "Division is wrong")
if __name__ == '__main__':
    unittest.main()