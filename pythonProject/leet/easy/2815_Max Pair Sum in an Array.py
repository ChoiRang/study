from typing import *
import collections

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = -1
        pair = collections.defaultdict(list)
        for num in nums:
            max_digit = int(max(str(num)))
            pair[max_digit].append(num)
        for key in pair.keys():
            if len(pair[key]) > 1:
                pair[key].sort(reverse=True)
                res = max(res, pair[key][0]+pair[key][1])

        return res
"""
max pair => 숫자중 가장 큰 숫자 기준의 페어를 뜻함, 테스트 케이스의 반대되는 숫자가 아님
"""