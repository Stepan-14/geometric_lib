import unittest
import circle
import rectangle
import square
import triangle


class GeometryTestCase(unittest.TestCase):
    # TESTS FOR RECTANGLE
      # area
    def test_rectangle_zero_mul(self):
        """Проверка площади прямоугольника, если одна сторона равна 0"""
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_rectangle_square_mul(self):
        """Проверка площади прямоугольника с равными сторонами"""
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_normal_rectangle_mul(self):
        """Проверка площади прямоугольника"""
        res = rectangle.area(10, 5)
        self.assertEqual(res, 50)

    def test_rectangle_negative_mul(self):
        """Проверка площади с отрицательным числом"""
        res = rectangle.area(-1, 5)
        self.assertEqual(res, "ERROR")

      # perimeter
    def test_rectangle_zero_perimeter(self):
        """Проверка периметра прямоугольника, если одна сторона равна 0"""
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, "ERROR")

    def test_rectangle_doublezero_perimeter(self):
        """Проверка периметра прямоугольника, все 4 стороны равны 0"""
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_normal_rectangle_perimeter(self):
        """Проверка периметра прямоугольника"""
        res = rectangle.perimeter(3, 4)
        self.assertEqual(res, 14)

    def test_rectangle_negative_perimeter(self):
        """Проверка периметра с отрицательным числом"""
        res = rectangle.perimeter(-1, 5)
        self.assertEqual(res, "ERROR")

    # TESTS FOR SQUARE
      # area
    def test_square_zero_mul(self):
        """Проверка площади квадрата со стороной 0"""
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_normal_square_mul(self):
        """Проверка площади квадрата"""
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_square_negative_mul(self):
        """Проверка площади квадрата с отрицательным числом"""
        res = square.area(-5)
        self.assertEqual(res, "ERROR")

      # perimeter
    def test_square_zero_perimeter(self):
        """Проверка периметра квадрата со стороной 0"""
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_normal_square_perimeter(self):
        """Проверка периметра квадрата"""
        res = square.perimeter(5)
        self.assertEqual(res, 20)

    def test_square_negative_perimeter(self):
        """Проверка периметра квадрата с отрицательным числом"""
        res = square.perimeter(-5)
        self.assertEqual(res, "ERROR")

    # TESTS FOR CIRCLE
      # area
    def test_circle_zero_mul(self):
        """Проверка площади круга с радиусом 0"""
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_normal_circle_mul(self):
        """Проверка площади круга"""
        res = circle.area(3)
        self.assertAlmostEqual(res, 28.2743, delta = 0.01)

    def test_circle_negative_mul(self):
        """Проверка площади круга с отрицательным числом"""
        res = circle.area(-3)
        self.assertEqual(res, "ERROR")

      # perimeter
    def test_circle_zero_perimeter(self):
        """Проверка периметра круга с радиусом 0"""
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_normal_circle_perimeter(self):
        """Проверка периметра круга"""
        res = circle.perimeter(3)
        self.assertAlmostEqual(res, 18.8495, delta = 0.01)

    def test_circle_negative_perimeter(self):
        """Проверка периметра круга с отрицательным числом"""
        res = circle.perimeter(-3)
        self.assertEqual(res, "ERROR")

    # TESTS FOR TRIANGLE
      # area
    def test_triangle_zero_mul(self):
        """Проверка площади треугольника, если одна сторона равна 0"""
        res = triangle.area(10, 5, 0)
        self.assertEqual(res, "ERROR")

    def test_normal_triangle_mul(self):
        """Проверка площади треугольника"""
        res = triangle.area(3, 4, 5)
        self.assertAlmostEqual(res, 6.0)

    def test_triangle_negative_mul(self):
        """Проверка площади треугольника с отрицательным числом"""
        res = triangle.area(-3, 4, 5)
        self.assertEqual(res, "ERROR")

      # perimeter
    def test_triangle_zero_perimeter(self):
        """Проверка периметра треугольника, если одна сторона равна 0"""
        res = triangle.perimeter(10, 5, 0)
        self.assertEqual(res, "ERROR")

    def test_normal_triangle_perimeter(self):
        """Проверка периметра треугольника"""
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_triangle_negative_perimeter(self):
        """Проверка периметра треугольника с отрицательным числом"""
        res = triangle.perimeter(-3, 4, 5)
        self.assertEqual(res, "ERROR")