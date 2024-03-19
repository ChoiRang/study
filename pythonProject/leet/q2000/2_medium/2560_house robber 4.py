from typing import *


class Solution:
	def minCapability(self, nums: List[int], k: int) -> int:
		N = len(nums)
		left = 0
		right = 10 ** 10

		def check(value):
			i = 0
			count = 0
			while i < N:
				if nums[i] <= value:
					i += 2
					count += 1
					continue
				i += 1
			return count >= k

		while left < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid + 1

		return left

"""
선택된 k 갯수 중 가장 큰 숫자중 작은 것을 고르는 문제

"""
