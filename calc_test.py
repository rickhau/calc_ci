# unittest_for_calc

import unittest
import calc

class CalcTestCase(unittest.TestCase):
	def setUp(self):
		self.args = (1, 2, 3)

	def tearDown(self):
		self.args = None

	def test_sum(self):
		expected = 6
		result = calc.sum(*self.args)
		self.assertEqual(expected, result)

if __name__ == "__main__":
	unittest.main()