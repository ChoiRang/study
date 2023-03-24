from typing import *


# REF
class Solution2:
	def evenOddBit(self, n: int) -> List[int]:
		i, even, odd = 0, 0, 0
		while n:
			if n % 2:
				if i % 2:
					odd += 1
				else:
					even += 1
			n //= 2
			i += 1
		return even, odd
"""
반환값이 2개면 리스트로 자동 변환.
"""


class Solution1:
	def evenOddBit(self, n: int) -> List[int]:
		print(bin(n))
		left, right = 0, 0
		for idx, num in enumerate(reversed(bin(n)[2:])):
			if idx % 2 == 0:
				left += int(num)
			else:
				right += int(num)

		return [left, right]
