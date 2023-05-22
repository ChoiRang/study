from typing import *


class Solution:
	def compress(self, chars: List[str]) -> int:
		N = len(chars)
		p1, p2 = 0, 0
		res = 0
		while p1 < N:
			while p2 < N and chars[p1] == chars[p2]:
				p2 += 1
			chars[res] = chars[p1]
			res += 1
			if (p2 - p1) > 1:
				for num in str(p2 - p1):
					chars[res] = num
					res += 1
			p1 = p2

		return res
