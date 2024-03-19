from typing import *


class Solution:
	def maxFrequency(self, nums: List[int], k: int) -> int:
		nums.sort()
		i, j, total = 0, 0, 0
		res = 0
		while j < len(nums):
			total += nums[j]

			while nums[j] * (j - i + 1) > total + k:
				total -= nums[i]
				i += 1
			res = max(res, j - i + 1)
			j += 1

		return res


"""
k번 연산 내에 같은 원소의 최대 갯수 구하기(k연산은 계산할때 마다 감소)
"""