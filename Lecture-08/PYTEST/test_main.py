# prompt: generate unit test for above code cell

import unittest
from main import function1

class TestFunction1(unittest.TestCase):

  def test_function1_positive_integers(self):
    self.assertEqual(function1(2, 3), 5)

  def test_function1_negative_integers(self):
    self.assertEqual(function1(-2, -3), -5)

  def test_function1_mixed_integers(self):
    self.assertEqual(function1(2, -3), -1)
    self.assertEqual(function1(-2, 3), 1)

  def test_function1_zero(self):
    self.assertEqual(function1(0, 5), 5)
    self.assertEqual(function1(5, 0), 5)
    self.assertEqual(function1(0, 0), 0)

# To run the tests in a Colab notebook, you can do the following:
# unittest.main(argv=['first-arg-is-ignored'], exit=False)