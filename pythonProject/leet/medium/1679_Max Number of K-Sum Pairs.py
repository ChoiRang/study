import collections
from typing import *


class Solution:
	def maxOperations(self, nums: List[int], k: int) -> int:
		N = len(nums)
		res = 0
		counter = collections.Counter(nums)
		numbers = counter.keys()

		for num in list(numbers):
			num_2 = k - num
			if num_2 in counter and num != num_2:
				val = min(counter[num_2], counter[num])
				counter[k - num] -= val
				counter[num] -= val
				res += val
			elif num_2 in counter:
				val = counter[num] // 2
				counter[num] -= val * 2
				res += val

		return res
