from typing import *
import collections


# REF n + 4*len(coordinates)
class Solution:
	def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
		count = collections.defaultdict(int)
		res = [0] * 5
		for x, y in coordinates:
			for nx in range(max(0, x - 1), min(m - 1, x + 1)):
				for ny in range(max(0, y - 1), min(n - 1, y + 1)):
					count[(nx, ny)] += 1

		for val in count.values():
			res[val] += 1

		res[0] = (m - 1) * (n - 1) - len(count.keys())

		return res


"""
nx -> 0 <= x < m and 0 <= x+1 < m
ny -> 0 <= y < n and 0 <= y+1 < n
(m - 1) * (n - 1) -> 총 block의 갯수
"""


# TLE 4mn + len(coordinates)
class Solution:
	def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
		dist = [[0, 0], [0, 1], [1, 0], [1, 1]]
		location = collections.defaultdict(list)
		res = [0] * 5
		for x, y in coordinates:
			location[x].append(y)

		for i in range(m - 1):
			for j in range(n - 1):
				count = 0
				for x, y in dist:
					nx, ny = i + x, j + y
					if ny in location[nx]:
						count += 1
				res[count] += 1

		return res
