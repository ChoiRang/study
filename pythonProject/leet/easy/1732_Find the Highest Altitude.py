from typing import *


class Solution1:
	def largestAltitude(self, gain: List[int]) -> int:
		res = [0]
		for num in gain:
			res.append(res[-1] + num)

		return max(res)
