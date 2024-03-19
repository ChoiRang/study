from typing import *


class Solution:
	def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
		result = []
		tmp = []
		count = 0
		for sc in score:
			tmp.append([sc[k], count])
			count += 1
		tmp.sort()
		for t in tmp[::-1]:
			result.append(score[t[1]])

		return result
