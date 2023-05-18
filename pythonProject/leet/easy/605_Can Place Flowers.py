from typing import *


class Solution:
	def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
		count = 0
		N = len(flowerbed)
		for i in range(N):
			if (i - 1 < 0 or flowerbed[i - 1] == 0) and \
					(flowerbed[i] == 0) and \
					(i + 1 >= N or flowerbed[i + 1] == 0):
				flowerbed[i] = 1
				count += 1
		return count >= n
