from typing import *


class Solution:
	def maxArea(self, height: List[int]) -> int:
		left, right, area = 0, len(height) - 1, 0
		while left < right:
			area = max(area, (min(height[left], height[right]) * (right - left)))
			if height[left] < height[right]:
				left += 1
			else:
				right -= 1

		return area


# TLE
class Solution1:
	def maxArea(self, height: List[int]) -> int:
		N = len(height)
		res = 0
		for i in range(N - 1):
			for j in range(i + 1, N):
				area = (j - i) * min(height[i], height[j])
				if area > res:
					res = area

		return res
