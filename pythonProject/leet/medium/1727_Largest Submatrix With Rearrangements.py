from typing import *


class Solution:
	def largestSubmatrix(self, matrix: List[List[int]]) -> int:
		m, n = len(matrix), len(matrix[0])

		for i in range(1, m):
			for j in range(n):
				if matrix[i][j] == 1:
					matrix[i][j] += matrix[i - 1][j]

		res = 0
		for i in range(m):
			matrix[i].sort(reverse=True)
			for j in range(n):
				res = max(res, matrix[i][j] * (j + 1))

		return res

"""
matrix[i][j] += matrix[i - 1][j] -> 연속된1의 높이 합
(j + 1) -> 가로 길이
"""