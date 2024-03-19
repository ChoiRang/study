from typing import *


class Solution:
	def findPrimePairs(self, n: int) -> List[List[int]]:
		primes = [0, 0] + [1] * n
		res = []
		for i in range(n):
			if primes[i] == 1:
				for j in range(i + i, n, i):
					primes[j] = 0
		for i in range(2, n // 2 + 1):
			if primes[i] and primes[n - i]:
				res.append([i, n - i])

		return res
