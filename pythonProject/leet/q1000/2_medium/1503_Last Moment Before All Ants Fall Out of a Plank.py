from typing import *


# 더 빠름
class Solution:
	def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
		return max(max(left) if left else 0, n - min(right) if right else 0)


class Solution1:
	def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
		left_time = [i for i in left]
		right_time = [n - i for i in right]

		return max(left_time + right_time)
