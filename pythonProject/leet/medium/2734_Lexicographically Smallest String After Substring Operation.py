class Solution:
	def smallestString(self, s: str) -> str:
		i = 0
		res = []
		while i < len(s) and ord(s[i]) == 97:
			res.append(s[i])
			i += 1

		operated = False
		while i < len(s) and ord(s[i]) > 97:
			operated = True
			res.append(chr(ord(s[i]) - 1))
			i += 1

		res.append(s[i:])
		if operated:
			return "".join(res)

		return s[:len(s) - 1] + "z"
