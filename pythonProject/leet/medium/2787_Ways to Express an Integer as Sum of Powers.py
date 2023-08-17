from functools import cache


class Solution:
	def numberOfWays(self, n: int, x: int) -> int:
		MOD = 10 ** 9 + 7

		@cache
		def get(idx, curr):
			if curr < 0:
				return 0
			if curr == 0:
				return 1

			p = pow(idx, x, MOD)
			if curr < p:
				return 0
			total = 0
			total += get(idx + 1, curr - p)
			total += get(idx + 1, curr)
			return total % MOD

		return get(1, n)


"""
get(1, 10) -> get(2, 9)	-> get(3, 5) -> 5 < 9 -> 0
												-> get(3, 9) -> 9-9 = 0 -> +1 
					-> get(2, 10)	-> get(3, 6) -> 6 < 9  -> 0
												-> get(3, 10) -> get(4, 1) -> 1 < 16 -> 0
																			-> get(4, 10) -> 10 < 16 -> 0
																			-------------------------------
																			total = 1
"""
