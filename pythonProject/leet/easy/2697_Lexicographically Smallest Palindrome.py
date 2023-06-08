class Solution:
	def makeSmallestPalindrome(self, s: str) -> str:
		N = len(s)
		n = len(s) // 2
		res = list(s)

		for i in range(n):
			if s[i] < s[N - i - 1]:
				res[N - i - 1] = s[i]
			elif s[i] > s[N - i - 1]:
				res[i] = s[N - i - 1]
		return "".join(res)
