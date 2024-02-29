import collections
import unittest
from typing import *


def solutions(n: int, bridge: List[int], start: int, dest: int) -> int:
	# ==========
	# n = int(input())
	# bridge = list(map(int,input().split()))
	# start, dest = map(int, input().split())
	# dest = int(input())-1
	# ==========
	def bfs():
		que = collections.deque([(start - 1, 0)])
		visited = [0] * n
		while que:
			curr, count = que.popleft()
			if curr == dest - 1:
				return count

			for i in range(curr, n, bridge[curr]):
				if not visited[i]:
					visited[i] = 1
					que.append((i, count + 1))
			for i in range(curr, -1, -bridge[curr]):
				if not visited[i]:
					visited[i] = 1
					que.append((i, count + 1))

		return -1

	return bfs()


class Test(unittest.TestCase):
	def test1(self):
		self.assertEqual(solutions(5, [1, 2, 2, 1, 2], 1, 5), 1)

	def test2(self):
		self.assertEqual(solutions(5, [2, 2, 1, 1, 2], 1, 5), 1)

	def test3(self):
		self.assertEqual(solutions(5, [3, 2, 1, 1, 2], 1, 5), 2)

	def test4(self):
		self.assertEqual(solutions(5, [5, 2, 1, 3, 2], 1, 5), -1)

	def test5(self):
		self.assertEqual(solutions(12, [3, 2, 1, 2, 2, 2, 3, 2, 4, 1, 2, 1], 1, 12), 2)

	def test6(self):
		self.assertEqual(solutions(12, [3, 2, 1, 5, 2, 2, 22, 2, 3, 11, 2, 1], 1, 12), 3)

	def test7(self):
		self.assertEqual(solutions(12, [3, 2, 1, 5, 2, 2, 22, 2, 6, 11, 2, 1], 1, 12), 4)
