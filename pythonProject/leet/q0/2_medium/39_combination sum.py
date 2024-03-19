from typing import *


class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		result = []

		def dfs(index, path):
			if sum(path) > target:
				return
			elif sum(path) == target:
				result.append(path)

			for i in range(index, len(candidates)):
				dfs(i, path + [candidates[i]])

		dfs(0, [])

		return result
