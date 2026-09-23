"""Unit tests for the Simple Calculator Application."""

import unittest
from calculator import add, subtract, multiply, divide, modulus, power


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""

    def test_add(self):
        """Test addition function."""
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        """Test subtraction function."""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        """Test multiplication function."""
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        """Test division function."""
        self.assertEqual(divide(10, 5), 2.0)
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_modulus(self):
        """Test modulus function."""
        self.assertEqual(modulus(11, 5), 1)
        self.assertEqual(modulus(10, 3), 1)

    def test_modulus_by_zero(self):
        """Test modulus by zero raises ValueError."""
        with self.assertRaises(ValueError):
            modulus(10, 0)

    def test_power(self):
        """Test exponentiation function."""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(3, 2), 9)


if __name__ == "__main__":
    unittest.main()
