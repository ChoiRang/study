from typing import *


class Solution:
	def getWinner(self, arr: List[int], k: int) -> int:
		if k > len(arr):
			return max(arr)
		max_num = arr[0]
		win_count = 0

		for i in range(1, len(arr)):
			if max_num > arr[i]:
				win_count += 1
			else:
				max_num = arr[i]
				win_count = 1

			if win_count == k:
				return max_num

		return max_num

"""
k 가 len(arr) 보다 크면 승자는 항상 큰수
"""