from typing import *


class Solution:
	def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
		select = sum(sorted([a - b for a, b in zip(reward1, reward2)], reverse=True)[:k])

		return sum(reward2) + select


"""
reward1=[1,1,3,4] reward2=[4,4,1,1] k=2, output=15
sum(reward2) = 10
reward1-reward2 = [-3, -3, 2, 3] => (2, 3) => choose 3,4 in reward1
reward2 choose 4, 4
sum(reawrd2) + (2, 3) = 15
"""
