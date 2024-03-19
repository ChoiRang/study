import collections
from typing import *


class Solution:
	def minOperations(self, nums: List[int]) -> int:
		count = collections.Counter(nums)
		res = 0
		for key in count.keys():
			if count[key] == 1:
				return -1
			num = count[key]
			res += min(self.check(num, 2), self.check(num, 3))

		return res

	def check(self, num, p):
		res, mod = divmod(num, p)
		if mod > 0: res += 1
		return res
