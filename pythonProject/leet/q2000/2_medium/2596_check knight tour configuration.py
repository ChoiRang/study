from typing import *


class Solution:
	def checkValidGrid(self, grid: List[List[int]]) -> bool:
		total_cell = len(grid) * len(grid[0])

		for line in grid:
			init_x = 0
			if 0 in line:
				init_y = line.index(0)
				break
			init_x += 1

		for i in range(1, total_cell):
			cordinate = []
			ver = 0
			for line in grid:
				if i in line:
					cordinate = [ver, line.index(i)]
					break
				ver += 1

			if abs(cordinate[0] - init_x) == 1 and abs(cordinate[1] - init_y) == 2:
				init_x = cordinate[0]
				init_y = cordinate[1]
			elif abs(cordinate[0] - init_x) == 2 and abs(cordinate[1] - init_y) == 1:
				init_x = cordinate[0]
				init_y = cordinate[1]
			else:
				return False

		return True
