from typing import *


class Solution:
	def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
		ver = []
		for i in range(len(nums)):
			for j in range(len(nums[i])):
				ver.append((i + j, j, nums[i][j]))
		ver.sort()

		return [i for _, _, i in ver]
