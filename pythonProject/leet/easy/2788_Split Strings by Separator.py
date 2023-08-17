from typing import *


class Solution:
	def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
		res = []
		for word in words:
			for w_s in word.split(separator):
				if w_s:
					res.append(w_s)

		return res
