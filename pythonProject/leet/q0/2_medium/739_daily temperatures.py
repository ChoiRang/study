from typing import *


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = idx - last
            stack.append(idx)

        return answer
