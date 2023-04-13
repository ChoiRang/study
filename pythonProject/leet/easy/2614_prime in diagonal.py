from typing import *
import math


class Solution:
	def diagonalPrime(self, nums: List[List[int]]) -> int:
		N = len(nums)
		calc_prime = lambda x: (x in (2, 3) or x % 6 in (1, 5)) and x > 1
		is_prime = lambda x: all(x % i for i in range(2, int(math.sqrt(x) + 1)))
		number = sorted(
			filter(calc_prime, {nums[i][i] for i in range(N)} | {nums[i][N - i - 1] for i in range(N)})
		)

		while number:
			num = number.pop()
			if is_prime(num):
				return num
		return 0
