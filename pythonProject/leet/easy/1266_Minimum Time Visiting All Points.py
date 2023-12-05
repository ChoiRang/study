from typing import *


class Solution:
	def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
		prev_x, prev_y = points[0][0], points[0][1]
		time = 0
		for x, y in points[1:]:
			time += max(abs(x - prev_x), abs(y - prev_y))
			prev_x, prev_y = x, y

		return time
