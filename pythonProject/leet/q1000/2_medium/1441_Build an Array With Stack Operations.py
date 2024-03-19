from typing import *


class Solution:
	def buildArray(self, target: List[int], n: int) -> List[str]:
		res = []
		curr = 1
		i = 0
		while curr <= n and i < len(target):
			num = target[i]
			if num == curr:
				res.append("Push")
				curr += 1
				i += 1
			else:
				res.append("Push")
				res.append("Pop")
				curr += 1

		return res
