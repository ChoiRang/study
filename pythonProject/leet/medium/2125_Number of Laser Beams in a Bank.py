from typing import *


class Solution:
	def numberOfBeams(self, bank: List[str]) -> int:
		count = []
		for row in bank:
			total = row.count('1')
			if total > 0: count.append(total)
		res = 0
		for i in range(len(count) - 1):
			res += count[i] * count[i + 1]

		return res
