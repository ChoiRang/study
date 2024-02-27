import unittest


def solutions(n: int, k: int) -> int:
	# n, k = map(int, input().split())
	tmp = n
	while bin(n).count("1") > k:
		n += 1

	return n - tmp


class Test(unittest.TestCase):
	def test1(self):
		self.assertEqual(solutions(3, 1), 1)

	def test2(self):
		self.assertEqual(solutions(13, 2), 3)

	def test3(self):
		self.assertEqual(solutions(1000000, 5), 15808)

	def test4(self):
		self.assertEqual(solutions(4, 1), 0)
