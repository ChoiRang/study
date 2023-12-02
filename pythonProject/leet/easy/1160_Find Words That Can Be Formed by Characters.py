from typing import *
import collections


class Solution:
	def countCharacters(self, words: List[str], chars: str) -> int:
		count = collections.Counter(chars)

		def check(word):
			word_count = collections.Counter(word)

			for key in word_count.keys():
				if word_count[key] > count[key]:
					return False
			return len(word)

		res = 0
		for w in words:
			res += check(w)

		return res
