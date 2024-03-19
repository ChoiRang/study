from typing import *


# TLE!
class Solution:
	def countWays(self, ranges: List[List[int]]) -> int:
		ranges.sort()
		overlap = [ranges[0]]
		for x, y in ranges[1:]:
			skip = False
			for idx, (x_1, y_1) in enumerate(overlap):
				if skip:
					continue

				if x_1 <= x <= y_1 and y >= y_1:
					overlap[idx] = [x_1, y]
					skip = True
				elif x_1 <= x <= y_1 and y <= y_1:
					overlap[idx] = [x_1, y_1]
					skip = True
				elif x <= x_1 and x_1 <= y <= y_1:
					overlap[idx] = [x, y_1]
					skip = True
				elif x <= x_1 and y >= y_1:
					overlap[idx] = [x, y]
					skip = True
				elif idx == len(overlap) - 1:
					overlap.append([x, y])

		N = len(overlap)

		return pow(2, N, 10 ** 9 + 7)


# REF
class Solution2:
	def countWays(self, ranges: List[List[int]]) -> int:
		pre = -1
		res = 0
		for a, b in sorted(ranges):
			res += pre < a
			pre = max(pre, b)

		return pow(2, res, 10 ** 9 + 7)
# 리스트 정렬 후 a 값이 이전의 b 보다 클 경우 1개의 분할이 생김
