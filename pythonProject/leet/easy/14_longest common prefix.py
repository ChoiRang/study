from typing import *


class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		MIN = min([len(word) for word in strs])
		res = ""
		for i in range(MIN):
			common = True
			init = strs[0][i]
			for word in strs[1:]:
				if word[i] != init:
					common = False
					break
			if common:
				res += init
			else:
				break

		return res


# REF
class SolutionREF1:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		if not strs:
			return ""
		strs.sort()
		first = strs[0]
		last = strs[-1]
		i = 0
		while i < len(first) and first[i] == last[i]:
			i += 1
		return first[:i]
"""
정렬하면 단어순으로 정렬됨, 첫번째와 마지막 단어가 가장 다름
"""
