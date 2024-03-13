class Solution:
	def minimumLength(self, s: str) -> int:
		i, j = 0, len(s) - 1
		while i < j and s[i] == s[j]:
			ch = s[i]
			while s[i + 1] == ch and i + 1 < j: i += 1
			while s[j - 1] == ch and i < j - 1: j -= 1
			if s[i] == ch: i += 1
			if s[j] == ch: j -= 1
		return j - i + 1
