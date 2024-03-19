import collections
from typing import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        count_k = collections.Counter(nums).most_common(k)
        for ck in count_k:
            answer.append(ck[0])

        return answer


class Solution2:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		count_k = list(zip(*collections.Counter(nums).most_common(k)))[0]

		return count_k
