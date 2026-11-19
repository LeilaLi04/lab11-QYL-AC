# https://github.com/LeilaLi04/lab11-QYL-AC
# Partner 1: Qingyao Li
# Partner 2: Atom Chahande
import unittest
import calculator

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-2, 3), 1)
        self.assertEqual(calculator.add(0, 4), 4)

    def test_subtract(self):
        self.assertEqual(calculator.sub(5, 2), 3)
        self.assertEqual(calculator.sub(2, 5), -3)
        self.assertEqual(calculator.sub(0, 5), -5)

   ######## Partner 1
    def test_multiply(self):
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(-2, 4), -8)
        self.assertEqual(calculator.mul(0, 5), 0)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5)
        self.assertEqual(calculator.div(4, 20), 5)
        self.assertEqual(calculator.div(-2, 8), -4)
    ##########################


    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)

    def test_logarithm(self):
        self.assertEqual(calculator.log(2, 8), 3)
        self.assertAlmostEqual(calculator.log(10, 100), 2)
        self.assertAlmostEqual(calculator.log(3, 9), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.log(-1, 8)

    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)
        self.assertAlmostEqual(calculator.hypotenuse(-3, 4), 5)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(9), 3)
        self.assertAlmostEqual(calculator.square_root(16), 4)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()