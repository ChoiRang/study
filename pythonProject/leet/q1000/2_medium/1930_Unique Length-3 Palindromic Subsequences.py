class Solution:
	def countPalindromicSubsequence(self, s: str) -> int:
		res = 0
		s_ch = set(s)

		for ch in s_ch:
			i = s.find(ch)
			j = s.rfind(ch)
			if i < j:
				res += len(set(s[i + 1: j]))

		return res

"""
*제한조건: 좌우 같은 문자열 길이는 3이다.
"""