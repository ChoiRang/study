from typing import *


class Solution:
	def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
		alp = {}
		for i in range(26):
			alp[i + 97] = i + 1
		for c, v in zip(chars, vals):
			alp[ord(c)] = v

		best = 0
		cur = 0
		for i in s:
			cur += alp[ord(i)]
			if cur < 0: cur = 0
			best = max(cur, best)

		return best
