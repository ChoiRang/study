from typing import *
import collections


class Solution:
	def findSpecialInteger(self, arr: List[int]) -> int:
		count = collections.Counter(arr)
		return count.most_common(1)[0][0]
