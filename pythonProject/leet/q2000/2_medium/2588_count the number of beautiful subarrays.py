import collections
from typing import *


class Solution:
	def beautifulSubarrays(self, nums: List[int]) -> int:
		seen = collections.Counter()
		count = 0
		current = 0
		seen[0] = 1
		for num in nums:
			current ^= num
			count += seen[current]
			seen[current] += 1

		return count


"""
[4, 3, 1, 2, 4] => xor(^) => [0] + [4, 7, 6, 4, 0]
idx = 0, 0 ^ 4 = 4 -> seen: No
idx = 1, 4 ^ 3 = 7 -> seen: No
idx = 2, 7 ^ 1 = 6 -> seen: No
idx = 3, 6 ^ 2 = 4 -> seen: 1 ([0, 4, 7, 6] => 4 1ea)
idx = 4, 1 ^ 4 = 0 -> seen: 1 ([0, 4, 7, 6, 4] => 0 1ea)
1 + 1 = 2


리스트의 숫자를 0 이 되도록 만든다. (xor)
(3, 1, 2) = (011, 001, 010) = 0

XOR 결과값 0 ~ j = x, 0 ~ i = x 일때 (i < j)
i+1 ~ j = x ^ x = 0, xor 의 결과값이 같은 부분 찾기
"""