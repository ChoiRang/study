from typing import *


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = []

        for i in range(len(digits)-1, -1, -1):
            if i == len(digits)-1:
                num, remain = divmod(digits[i]+1, 10)
            else:
                num, remain = divmod(digits[i]+num, 10)
            answer[0:0] = [remain]

        if num == 1:
            answer[0:0] = [num]

        return answer
