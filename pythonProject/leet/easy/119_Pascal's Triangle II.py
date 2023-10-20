from typing import *


class Solution:
	def getRow(self, rowIndex: int) -> List[int]:
		res = [1]
		prev = 1
		for i in range(1, rowIndex + 1):
			val = prev * (rowIndex - i + 1) // i
			res.append(val)
			prev = val

		return res
