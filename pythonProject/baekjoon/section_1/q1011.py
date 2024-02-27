import sys
import unittest


def solutions(x, y):
	# n = int(sys.stdin.readline())
	# [map(int, sys.stdin.readline().split()) for _ in range(n)]
	res = 0
	while y - x > res * (res + 1):
		res += 1
	return 2*res - ((y-x) <= res ** 2)


class Test(unittest.TestCase):
	def test1(self):
		self.assertEqual(solutions(0, 3), 3)

	def test2(self):
		self.assertEqual(solutions(1, 5), 3)

	def test3(self):
		self.assertEqual(solutions(0, 15), 7)

	def test4(self):
		self.assertEqual(solutions(0, 16), 7)

	def test5(self):
		self.assertEqual(solutions(0, 17), 8)

	def test6(self):
		self.assertEqual(solutions(0, 20), 8)

	def test7(self):
		self.assertEqual(solutions(0, 21), 9)
