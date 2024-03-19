from typing import *


class Solution:
	def minCost(self, nums: List[int], x: int) -> int:
		n = len(nums)
		costs = [i * x for i in range(n)]

		for i in range(n):
			curr = nums[i]
			for j in range(n):
				curr = min(curr, nums[(i + j) % n])
				costs[j] += curr

		return min(costs)


"""
((i + 1) mod n)^th -> n = n+1, 한번의 시행 후 좌로 한칸씩 밀 수 있다.
costs[i] = i 번 수행후의 값
curr = min(nums[i-k], ... , nums[i-1], nums[i])
"""
