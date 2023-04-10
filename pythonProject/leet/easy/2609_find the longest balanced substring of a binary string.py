class Solution:
	def findTheLongestBalancedSubstring(self, s: str) -> int:
		tmp = "01"
		res = 0
		while len(tmp) <= len(s):
			if tmp in s:
				res = len(tmp)
			tmp = '0' + tmp + '1'
		return res


"""
all zeroes are before ones -> 01 기준
"""
