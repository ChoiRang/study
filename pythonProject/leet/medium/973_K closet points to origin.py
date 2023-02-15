from typing import *


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_idx = []
        for idx, (x, y) in enumerate(points):
            k_idx.append([x**2+y**2, idx])
        k_idx.sort()
        result = [points[k_idx[i][1]] for i in range(k)]

        return result
