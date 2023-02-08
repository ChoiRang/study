from typing import *


class Solution:
	def pickGifts(self, gifts: List[int], k: int) -> int:
		for _ in range(k):
			max_val = max(gifts)
			max_idx = gifts.index(max_val)

			sqrt_val = int(math.sqrt(max_val))
			gifts[max_idx] = sqrt_val

		return sum(gifts)
