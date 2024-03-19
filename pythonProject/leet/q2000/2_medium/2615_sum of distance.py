from typing import *
import collections


class Solution:
	def distance(self, nums: List[int]) -> List[int]:
		N = len(nums)
		counter = collections.defaultdict(list)
		res = [0] * N
		for idx, num in enumerate(nums):
			counter[num].append(idx)

		for num in counter.keys():
			idxs = counter[num]
			total = 0
			for i in range(1, len(idxs)):
				total += idxs[i] - idxs[0]
			res[idxs[0]] = total

			for i in range(1, len(idxs)):
				total += (idxs[i] - idxs[i - 1]) * (i + 1)
				total -= (idxs[i] - idxs[i - 1]) * (len(idxs) - i + 1)
				res[idxs[i]] = total

		return res
