from typing import *
import math


class Solution:
	def countBeautifulPairs(self, nums: List[int]) -> int:
		res = 0
		n = len(nums)
		for i in range(n):
			for j in range(i + 1, n):
				res += math.gcd(int(str(nums[i])[0]), int(str(nums[j])[-1])) == 1

		return res
