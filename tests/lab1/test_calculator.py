"""Тесты для калькулятора"""
import unittest

from src.lab1.calculator import calculator


class CalculatorTestCase(unittest.TestCase):
    """Набор тестов проверок простых операций"""

    def test_addition(self):
        """Проверка сложения"""
        self.assertEqual(calculator(2, "+", 3), 5)

    def test_subtraction(self):
        """Проверка вычитания"""
        self.assertEqual(calculator(10, "-", 4), 6)

    def test_multiplication(self):
        """Проверка умножения"""
        self.assertEqual(calculator(3, "*", 7), 21)

    def test_division(self):
        """Проверка деления"""
        self.assertEqual(calculator(8, "/", 2), 4)

    def test_division_by_zero(self):
        """Проверка деления на 0"""
        with self.assertRaises(ValueError):
            calculator(1, "/", 0)

    def test_unknown_operation(self):
        """Проверка ввода неизвестной операции"""
        with self.assertRaises(ValueError):
            calculator(1, "$", 3)


if __name__ == "__main__":
    unittest.main()
