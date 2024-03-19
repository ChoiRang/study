class Solution:
	def countHomogenous(self, s: str) -> int:
		MOD = 10 ** 9 + 7
		res, count = 0, 0
		prev_ch = "?"

		for ch in s:
			if prev_ch == ch:
				count += 1
			else:
				count = 1
				prev_ch = ch
			res += count
			res %= MOD

		return res
