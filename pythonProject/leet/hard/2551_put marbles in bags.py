from typing import *


class Solution:
	def putMarbles(self, weights: List[int], k: int) -> int:
		# split k-1 times
		split_point = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]

		split_point.sort()
		L = len(split_point)
		max_val, min_val = 0, 0
		for i in range(k - 1):
			max_val += split_point[L - i - 1]
			min_val += split_point[i]

		return max_val - min_val


"""
좌우 끝은 최대 or 최소 값에서 항상 동일(제외)
ref: heapq.nlargest(k-1, split_point), heapq.nsmallest(k-1, split_point)
"""