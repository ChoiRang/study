from typing import *


# 86ms
class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		per = []

		def dfs(idx_list: List[int], per_num: List[int], count):
			if count == len(nums):
				per.append(per_num)
				return

			for idx, num in enumerate(nums):
				if idx not in idx_list:
					per_num_pre, idx_list_pre = per_num[:], idx_list[:]
					per_num.append(num)
					idx_list.append(idx)

					dfs(idx_list, per_num, count + 1)
					idx_list, per_num = idx_list_pre, per_num_pre

		dfs([], [], 0)

		return per


# ref, 39ms
class Solution2:
	def permute(self, nums: List[int]) -> List[List[int]]:
		result = []
		prev_elements = []

		def dfs(elements):
			if len(elements) == 0:
				result.append(prev_elements[:])

			for e in elements:
				next_elements = elements[:]
				next_elements.remove(e)

				prev_elements.append(e)
				dfs(next_elements)
				prev_elements.pop()

		dfs(nums)
		return result


# itertools -> permutation
import itertools


class Solution3:
	def permute(self, nums: List[int]) -> List[List[int]]:
		return itertools.permutations(nums)
