from typing import *


class Solution:
	def divisibilityArray(self, word: str, m: int) -> List[int]:
		answer = []
		num = 0
		for i in word:
			num *= 10
			num += int(i)
			num = pow(num, 1, m)

			if num == 0:
				answer.append(1)
			else:
				answer.append(0)

		return answer


"""
int("1") < ord("1") - ord("0")
"""