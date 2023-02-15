from typing import *


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result = [-1, 10**4]
        for idx, (p_x, p_y) in enumerate(points):
            if p_x == x or p_y == y:
                dist = abs(x-p_x) + abs(y-p_y)
                if dist < result[1]:
                    result[0] = idx
                    result[1] = dist

        return result[0]
