import collections


# REF
class Solution2:
	def findTheDifference(self, s: str, t: str) -> str:
		t_count = collections.Counter(t)
		s_count = collections.Counter(s)
		for ch in t_count:
			if t_count[ch] != s_count[ch]:
				return ch
	"""
	for 문 보다 Counter 가 속도 빠름, 메모리 더 낮음
	"""


class Solution:
	def findTheDifference(self, s: str, t: str) -> str:
		count = collections.Counter(t)
		for i in s:
			count[i] -= 1
		return count.most_common()[0][0]
