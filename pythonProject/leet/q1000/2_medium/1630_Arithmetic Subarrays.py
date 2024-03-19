from typing import *


class Solution:
	def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
		res = []

		for i in range(len(l)):
			sub = sorted(nums[l[i]:r[i] + 1])
			inc = sub[1] - sub[0]
			for j in range(2, len(sub)):
				if sub[j] - sub[j - 1] != inc:
					res.append(False)
					break

			if len(res) < i + 1:
				res.append(True)

		return res
