from typing import *


class Solution:
	def findMinArrowShots(self, points: List[List[int]]) -> int:
		points.sort(key=lambda x: x[0])
		res = 1
		p = points[0][1]
		for i in range(1, len(points)):
			start, end = points[i]
			if start > p:
				res += 1
				p = end
			else:
				p = min(p, end)

		return res
