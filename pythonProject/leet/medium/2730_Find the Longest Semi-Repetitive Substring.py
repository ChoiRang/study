class Solution:
	def longestSemiRepetitiveSubstring(self, s: str) -> int:
		left = 0
		count = 0
		res = 1
		for right in range(1, len(s)):
			if s[right] == s[right - 1]:
				count += 1
			while count > 1:
				if s[left] == s[left + 1]:
					count -= 1
				left += 1
			res = max(res, right - left + 1)
		return res

"""
Semi-Repetitive = 문자열 특정 구간내 동일한 숫자의 페어(붙어있는)가 최대 1개
"""
