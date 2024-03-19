from collections import defaultdict
from typing import *


# REF
class Solution:
	def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
		m = defaultdict(lambda: [-1, -1])
		for i, ch in enumerate(s):
			val = 0
			for j in range(i, min(i + 30, len(s))):
				val = val * 2 + ord(s[j]) - ord("0")
				if val not in m:
					m[val] = [i, j]
				if ch == "0":
					break
		return [m[f ^ s] for f, s in queries]


# TLE
class Solution:
	def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
		# val == second_i ^ first_i
		N = len(s)
		result = []
		values = {}
		for i in range(N):
			for j in range(i + 1, N + 1):
				zero_count = len(s[i:j]) - len(str(int(s[i:j])))
				sub = int(s[i: j], 2)
				if sub not in values:
					values[sub] = [i + zero_count, j - 1]

		for query in queries:
			val = query[0] ^ query[1]
			if val in values:
				x, y = values[val]
				result.append([x, y])
			else:
				result.append([-1, -1])

		return result
