import heapq
from math import ceil
from typing import List


# timeovr
class Solution1:
    def maxKelements(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(k):
            sort_nums = sorted(nums)
            max_num = sort_nums.pop()
            result += max_num
            sort_nums.append(ceil(max_num/3))
            nums = sort_nums

        return result


class Solution2:
    def maxKelements(self, nums: List[int], k: int) -> int:
        result = 0
        heap = []

        for i in nums:
            heapq.heappush(heap, -i)

        for _ in range(k):
            num = -heapq.heappop(heap)
            result += num
            heapq.heappush(heap, -ceil(num/3))

        return result
