from typing import *
import collections


# REF
class Solution:
	def countNicePairs(self, nums: List[int]) -> int:
		modified = [i - int(str(i)[::-1]) for i in nums]

		count = 0
		for i in Counter(modified).values():
			count += i * (i - 1) // 2
		return count % (1000000000 + 7)


class Solution1:
	def countNicePairs(self, nums: List[int]) -> int:
		MOD = 10 ** 9 + 7

		total = 0
		seen = collections.Counter()
		for num in nums:
			ans = 0
			pair = num
			while num > 0:
				ans *= 10
				num, re = divmod(num, 10)
				ans += re
			pair -= ans
			total += seen[pair]
			seen[pair] += 1

		return total % MOD


"""
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
=> nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
"""
