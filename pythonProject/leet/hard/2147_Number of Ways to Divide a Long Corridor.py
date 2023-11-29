class Solution:
	def numberOfWays(self, corridor: str) -> int:
		MOD = 10 ** 9 + 7
		res, s, p = 1, 0, 0
		for ch in corridor:
			if ch == "S":
				s += 1
				if s == 3:
					res = res * (p + 1)
					s, p = 1, 0
			else:
				if s == 2:
					p += 1

		if s != 2:
			return 0

		return res % MOD
