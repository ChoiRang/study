import unittest
from typing import *


def solution(butter: List[List[int]]):
	# =======================
	# n = int(sys.stdin.readline())
	# butter = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
	# =======================
	n = len(butter)
	# =======================
	butter.sort(key=lambda x: x[0])
	prev_loc = butter[0][0]
	prev_h = butter[0][1]
	MOD = 10 ** 100
	res = MOD
	for i in range(1, n):
		curr_loc, curr_h = butter[i][0], butter[i][1]
		dist = curr_loc - prev_loc - 1
		min_dist = min(prev_h, curr_h) // 2
		max_dist = max(prev_h, curr_h) // 2 - min_dist
		if min_dist > dist // 2:
			res = min(res, dist // 2)
		elif max_dist > dist - min_dist*2:
			res = min(res, dist - min_dist)

		prev_loc, prev_h = curr_loc, curr_h
	return "forever" if res == MOD else res


class Test(unittest.TestCase):
	def test1(self):
		self.assertEqual(solution([[1, 3], [5, 7]]), 2)

	def test2(self):
		self.assertEqual(solution([[5, 5], [1, 5]]), 1)

	def test3(self):
		self.assertEqual(solution([[-1, 1], [19191919, 7], [100, 3]]), "forever")

	def test4(self):
		self.assertEqual(solution([[1, 1], [5, 7]]), "forever")

	def test5(self):
		self.assertEqual(solution([[1, 1], [5, 99]]), 3)

	def test6(self):
		self.assertEqual(solution([[1, 1], [5, 5]]), "forever")

	def test7(self):
		self.assertEqual(solution([[1, 3],[5, 5]]), "forever")

	def test8(self):
		self.assertEqual(solution([[1, 3], [5, 7], [11, 7]]), 2)

	def test9(self):
		self.assertEqual(solution([[1, 3], [5, 5], [7, 3]]), 0)

	def test10(self):
		self.assertEqual(solution([[1, 5], [6, 5]]), "forever")

	def test11(self):
		self.assertEqual(solution([[1, 5], [6, 7]]), 2)

	def test12(self):
		self.assertEqual(solution([[1, 3], [6, 7]]), "forever")

	def test13(self):
		self.assertEqual(solution([[1, 5], [6, 7]]), 2)

	def test14(self):
		self.assertEqual(solution([[11, 23], [3999, 222], [1, 11]]), 4)

	def test15(self):
		self.assertEqual(solution([[1, 11], [7, 23]]), 2)

	def test16(self):
		self.assertEqual(solution([[1, 11], [8, 23]]), 3)

	def test17(self):
		self.assertEqual(solution([[1, 7], [8, 7]]), "forever")

	def test18(self):
		self.assertEqual(solution([[1, 7], [8, 9]]), 3)
