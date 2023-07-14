from typing import *


class Solution:
	def maximumNumberOfStringPairs(self, words: List[str]) -> int:
		total = 0
		seen = set()
		for word in words:
			if word in seen:
				total += 1
			else:
				seen.add(word[::-1])

		return total
