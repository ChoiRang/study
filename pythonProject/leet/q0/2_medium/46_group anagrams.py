from typing import *
from collections import defaultdict


class Solution:
	def group_anagrams(self, strs: List[str]) -> List[List[str]]:
		anagrams = defaultdict(list)

		for word in strs:
			anagrams[''.join(sorted(word))].append(word)

		return list(anagrams.values())