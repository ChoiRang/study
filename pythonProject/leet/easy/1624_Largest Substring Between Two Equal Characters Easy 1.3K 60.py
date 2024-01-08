class Solution:
	def maxLengthBetweenEqualCharacters(self, s: str) -> int:
		ord_set = [-1] * 27
		res = -1
		for i, ch in enumerate(s):
			if ord_set[ord(ch) - 97] > -1:
				res = max(res, i - ord_set[ord(ch) - 97] - 1)
			else:
				ord_set[ord(ch) - 97] = i

		return res
