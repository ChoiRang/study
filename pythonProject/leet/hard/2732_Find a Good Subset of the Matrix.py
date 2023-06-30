from typing import *


class Solution:
	def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
		rows = {}

		for idx, row in enumerate(grid):
			total = sum(1 << i for i, x in enumerate(row) if x)
			if total == 0: return [idx]
			for row_sum in rows:
				if total & row_sum == 0:
					return [rows[row_sum], idx]
			rows[total] = idx

		return []


"""
같은 해답, dict() 가 list 보다 속도 빠름 (ex 5255-> 175)ms
"""


# TLE
class Solution1:
	def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
		res = []

		for idx, row in enumerate(grid):
			total = sum(1 << i for i, x in enumerate(row) if x)
			if total == 0: return [idx]
			for i in range(len(res)):
				if total & res[i] == 0:
					return [i, idx]
			res.append(total)

		return []


"""
k = 각 컬럼의 합이 floor(len(grid[0]) / 2)보다 작아야 함 -> 값이 0,1 둘중 하나만 존재하므로, 각 칼럼의 합이 1 이하이면 조건 충족
& => (bitwise and, 두 숫자가 1이면 1 그 외 0)
[1,1,1,1],[0,1,1,0] -> [1,2,4,8],[0,2,4,0] -> total = [15], [6]
15 & 6 == 6
 0b1111
&0b 110
-------
 0b 110 => 6
-------------
[0,1,1,0],[0,0,0,1] -> [0,2,4,0],[0,0,0,8] -> total = [6], [8]
6 & 8 == 0
 0b1000
&0b 110
-------
 0b0 => 0
=======
 
"""
