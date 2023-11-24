from typing import *


class Solution:
	def maxCoins(self, piles: List[int]) -> int:
		piles.sort(reverse=True)
		res = 0

		for i in range(len(piles) // 3):
			res += piles[i * 2 + 1]

		return res
