import unittest


def solutions(n, m, a, b) -> int:
	# n, m = map(int, input().split())
	# a = [list(map(int,stdin.readline().rstrip())) for _ in range(n)]
	# b = [list(map(int, stdin.readline().rstrip())) for _ in range(m)]
	def flip(x, y):
		for i in range(x, x + 3):
			for j in range(y, y + 3):
				if a[i][j] == 0:
					a[i][j] = 1
				else:
					a[i][j] = 0

	res = 0
	for i in range(n - 2):
		for j in range(m - 2):
			if a[i][j] != b[i][j]:
				flip(i, j)
				res += 1
	if a == b:
		return res

	return -1


class Test(unittest.TestCase):
	def test1(self):
		self.assertEqual(
			solutions(3, 4, [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]], [[1, 0, 0, 1], [1, 0, 1, 1], [1, 0, 0, 1]]), 2)

	def test2(self):
		self.assertEqual(solutions(3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 1)

	def test3(self):
		self.assertEqual(solutions(1, 1, [[1]], [[0]]), -1)

	def test4(self):
		self.assertEqual(solutions(3, 3, [[1, 1, 1], [0, 0, 0], [1, 1, 1]], [[1, 1, 1], [0, 0, 0], [1, 1, 1]]), 0)

	def test5(self):
		self.assertEqual(solutions(3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[0, 1, 0], [0, 0, 0], [0, 0, 0]]), -1)
