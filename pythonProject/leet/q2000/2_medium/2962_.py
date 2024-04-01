from typing import *


class Solution:
	def countSubarrays(self, nums: List[int], k: int) -> int:
		max_num = max(nums)
		left = 0
		res = 0
		count = 0
		for i, num in enumerate(nums):
			if num == max_num:
				count += 1
			while count >= k:
				if nums[left] == max_num:
					count -= 1
				left += 1
			res += left
		return res
