import bisect
from typing import *


# timeout
class Solution:
	def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
		N = len(nums)
		count = 0

		for i in range(N - 1):
			for j in range(i + 1, N):
				num = nums[i] + nums[j]
				if lower <= num <= upper:
					count += 1

		return count


# REF
class Solution2:
	def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
		# lower <= x+y <= upper
		# lower-x <= y <= upper-x
		total = 0
		nums.sort()

		for x in nums:
			low = bisect.bisect_left(nums, lower - x)
			high = bisect.bisect(nums, upper - x)
			count = high - low
			if lower - x <= x <= upper - x:
				count -= 1
			total += count

		return total // 2
