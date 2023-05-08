import collections
from typing import *


# SLOW,
class Solution:
	def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
		counter = collections.Counter()
		res = []
		for num1, num2 in zip(A, B):
			counter[num1] += 1
			counter[num2] += 1
			max_count = 2
			total = 0
			for num, count in counter.most_common():
				if count < max_count:
					break
				if count >= max_count:
					count = max_count
					total += 1
			res.append(total)

		return res


# REF
class Solution:
	def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
		cur = 0
		sta, stb = set(), set()
		ans = []
		for i in range(len(A)):
			sta.add(A[i])
			stb.add(B[i])
			if B[i] in sta:
				cur += 1
			if A[i] in stb and B[i] != A[i]:
				cur += 1
			ans.append(cur)
		return ans
