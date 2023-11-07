from typing import *


# REF ( O(2n) )
class Solution:
	def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
		res = 0
		priority = [i / j for i, j in zip(dist, speed)]
		priority.sort()

		for i in range(len(dist)):
			if priority[i] > i:
				res += 1
			else:
				break

		return res


# TLE ( O(n ** 2) )
class Solution1:
	def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
		n = len(dist)
		res = 0
		while res < n:
			zero = 0
			for i in range(n):
				dist[i] -= speed[i]
				if dist[i] <= 0:
					zero += 1

			if zero - res > 1:  # ***
				return res + 1

			res += 1

		return res
