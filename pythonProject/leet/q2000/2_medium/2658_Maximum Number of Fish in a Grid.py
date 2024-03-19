from typing import *


class Solution:
	def findMaxFish(self, grid: List[List[int]]) -> int:
		max_fish = 0
		M, N = len(grid), len(grid[0])
		move_dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

		def move(r, c):
			total = grid[r][c]
			grid[r][c] = 0
			for x, y in move_dir:
				new_x, new_y = r + x, c + y
				if 0 <= new_x < M and 0 <= new_y < N and grid[new_x][new_y] > 0:
					total += move(new_x, new_y)

			return total

		for x in range(M):
			for y in range(N):
				if grid[x][y] > 0:
					print(x, y)
					max_fish = max(max_fish, move(x, y))

		return max_fish
