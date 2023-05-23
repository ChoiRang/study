class Solution:
	def maxVowels(self, s: str, k: int) -> int:
		vowels = "aeiou"
		cur_ch = s[:k]
		cur = res = len([i for i in cur_ch if i in vowels])
		for i in range(len(s) - k):
			if s[i] in vowels:
				cur -= 1
			if s[i + k] in vowels:
				cur += 1
			res = max(res, cur)

		return res
