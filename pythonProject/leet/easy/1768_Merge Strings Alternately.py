class Solution:
	def mergeAlternately(self, word1: str, word2: str) -> str:
		N = min(len(word1), len(word2))
		res = []
		for i in range(N):
			res.append(word1[i])
			res.append(word2[i])
		res.append(word1[N:])
		res.append(word2[N:])
		return ''.join(res)
