import math
import unittest


def bridge_possible(n, m):
	return math.factorial(m) // (math.factorial(n)*math.factorial(m-n))


class Test(unittest.TestCase):
	def test1(self):
		self.assertEqual(bridge_possible(2, 2), 1)

	def test2(self):
		self.assertEqual(bridge_possible(1, 5), 5)

	def test3(self):
		self.assertEqual(bridge_possible(13, 29), 67863915)

	def test4(self):
		self.assertEqual(bridge_possible(3, 5), 10)
