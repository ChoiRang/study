class Solution:
	def addMinimum(self, word: str) -> int:
		curr, prev = 0, 'z'
		for w in word:
			if w <= prev:
				curr += 1
			prev = w

		return curr * 3 - len(word)
