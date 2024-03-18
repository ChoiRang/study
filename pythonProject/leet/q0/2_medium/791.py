import collections


class Solution:
	def customSortString(self, order: str, s: str) -> str:
		counter = collections.Counter(s)
		res = ""
		for c in order:
			if c in s:
				if counter[c] > 0:
					res += (c * counter[c])
					counter[c] = 0

		for c in counter.keys():
			if counter[c] > 0:
				res += (c * counter[c])

		return res

