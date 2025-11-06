import unittest
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()

    def test_add(self):
        """Test addition functionality."""

        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(5, 7), 12)
        
        self.assertEqual(self.calc.add(-1, -2), -3)
        self.assertEqual(self.calc.add(-5, 3), -2)

        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_multiply(self):
        """Test multiplication functionality."""

        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(2, 5), 10)

        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_subtract(self):
        """Test subtraction functionality."""

        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 4), 6)

        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(5, -3), 8)
        
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_divide(self):
        """Test division functionality."""

        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(15, 3), 5)

        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.33333, places=4)
        
    def test_divide_by_zero(self):
        """Test that division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
        
        with self.assertRaises(ValueError):
            self.calc.divide(-5, 0)

