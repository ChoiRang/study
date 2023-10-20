class Solution:
	def backspaceCompare(self, s: str, t: str) -> bool:
		def get_back(s):
			n = len(s)
			i = n - 1
			skip = 0
			res = ""
			while i > -1:
				if s[i] == '#':
					skip += 1
					i -= 1
					continue
				if skip > 0:
					i -= 1
					skip -= 1
				else:
					res += s[i]
					i -= 1
			return res

		return get_back(s) == get_back(t)


