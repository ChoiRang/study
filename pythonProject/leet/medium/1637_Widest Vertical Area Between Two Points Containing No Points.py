from typing import *


class Solution:
	def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
		points.sort()
		prev = points[0][0]
		res = 0
		for x, _ in points[1:]:
			curr = x - prev
			if curr > res:
				res = curr
			prev = x
		return res
