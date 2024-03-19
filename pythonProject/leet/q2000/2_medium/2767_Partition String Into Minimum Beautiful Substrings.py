class Solution:
	def minimumBeautifulSubstrings(self, s: str) -> int:
		res = 0
		n = len(s)
		p5 = [str(bin(5 ** i))[2:] for i in range(7)]
		idx = 0

		def sub_str(idx):
			if idx == n:
				return 0
			best = 20
			for p in p5:
				if s[idx:].startswith(p):
					best = min(best, sub_str(idx + len(p)) + 1)

			return best

		res = sub_str(0)

		return -1 if res == 20 else res
