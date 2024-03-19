from typing import *


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0]*n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                top_left, bottom_right = set(), set()

                x1, y1 = x+1, y+1
                while x1 < m and y1 < n:
                    bottom_right.add(grid[x1][y1])
                    x1 += 1
                    y1 += 1

                x2, y2 = x-1, y-1
                while x2 >= 0 and y2 >=0:
                    top_left.add(grid[x2][y2])
                    x2 -= 1
                    y2 -= 1

                res[x][y] = abs(len(bottom_right)-len(top_left))
        return res

"""
각 셀 기준 대각선(좌상단~우하단)끝까지 고유한 숫자의 차이
1번째 예시에는 9가지중 3가지의 경우만 있다.
"""