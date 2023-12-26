from typing import *


class Solution:
	def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
		m, n = len(img), len(img[0])
		res = [[0] * n for _ in range(m)]
		dist = [[-1, -1], [-1, 0], [-1, 1],
						[0, -1], [0, 0], [0, 1],
						[1, -1], [1, 0], [1, 1]]
		for i in range(m):
			for j in range(n):
				total, count = 0, 0
				for x, y in dist:
					nx, ny = x + i, y + j
					if 0 <= nx < m and 0 <= ny < n:
						total += img[nx][ny]
						count += 1
				res[i][j] = total // count

		return res
