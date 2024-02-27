import unittest


def solutions(n: int, r: int, c: int) -> int:
	def dfs(n, r, c):
		if n == 0:
			return 0
		return 2*(r%2)+c%2 + 4 * dfs(n - 1, r // 2, c // 2)

	return dfs(n, r, c)


class Test(unittest.TestCase):
	def test1(self):
		self.assertEqual(solutions(2, 3, 1), 11)

	def test2(self):
		self.assertEqual(solutions(3, 7, 7), 63)

	def test3(self):
		self.assertEqual(solutions(1, 0, 0), 0)

	def test4(self):
		self.assertEqual(solutions(4, 7, 7), 63)

	def test5(self):
		self.assertEqual(solutions(10, 511, 511), 262143)

	def test6(self):
		self.assertEqual(solutions(10, 512, 512), 786432)

	def test7(self):
		self.assertEqual(solutions(3, 4, 3), 37)
