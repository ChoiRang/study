from typing import *
import collections


class Solution:
	def longestValidSubstring(self, words: str, forbidden: List[str]) -> int:
		n = len(words)
		res = 0
		seen = set(forbidden)
		max_f = max([len(s) for s in forbidden])

		def check():
			n2 = len(curr)
			word = ""
			for i in range(1, max_f + 1):
				if n2 - i < 0:
					break
				word = curr[n2 - i] + word
				if word in seen:
					return True
			return False

		curr = collections.deque()

		for right in range(n):
			curr.append(words[right])
			while check():
				curr.popleft()
			res = max(res, len(curr))

		return res
