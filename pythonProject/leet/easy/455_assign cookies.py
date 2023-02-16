from typing import *


class Solution:
	def findContentChildren(self, g: List[int], s: List[int]) -> int:
		g.sort(reverse=True)
		s.sort(reverse=True)
		count = 0
		while g and s:
			if s[-1] >= g[-1]:
				count += 1
				g.pop()
				s.pop()
			else:
				s.pop()

			if len(g) == 0 or len(s) == 0:
				return count

		return count
