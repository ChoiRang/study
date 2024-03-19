from functools import lru_cache
from typing import *


class Solution:
	def minimizeConcatenatedLength(self, words: List[str]) -> int:
		n = len(words)

		@lru_cache(maxsize=None)
		def dfs(index, front, rear):
			if index == n:
				return 0
			word = words[index]
			cost = len(word)
			best = 1000 * 50 + 1
			if word[0] == rear:
				best = min(best, dfs(index + 1, front, word[-1]) + cost - 1)
			else:
				best = min(best, dfs(index + 1, front, word[-1]) + cost)
			if word[-1] == front:
				best = min(best, dfs(index + 1, word[0], rear) + cost - 1)
			else:
				best = min(best, dfs(index + 1, word[0], rear) + cost)
			return best

		cost = dfs(1, words[0][0], words[0][-1])

		return cost + len(words[0])
