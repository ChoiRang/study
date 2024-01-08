from typing import *


class Solution:
	def makeEqual(self, words: List[str]) -> bool:
		ord_word = [0] * 26
		for word in words:
			for ch in word:
				ord_word[ord(ch) - 97] += 1

		n = len(words)
		for i in ord_word:
			if i % n != 0:
				return False
		return True
