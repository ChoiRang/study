from typing import *


class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		phone_number = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
										"6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

		if not digits:
			return []

		answer = []
		for digit in digits:
			tmp = []
			if answer:
				for i in answer:
					for j in phone_number[digit]:
						tmp.append(i + j)
				answer = tmp
			else:
				for i in phone_number[digit]:
					answer.append(i)

		return answer
