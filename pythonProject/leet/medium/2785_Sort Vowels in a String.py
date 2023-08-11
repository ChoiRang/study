class Solution:
	def sortVowels(self, s: str) -> str:
		vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
		idxs = []
		vowel = []
		s = [i for i in s]
		for i, ch in enumerate(s):
			if ch in vowels:
				idxs.append(i)
				vowel.append(ch)

		vowel.sort()
		for i, idx in enumerate(idxs):
			s[idx] = vowel[i]

		return ''.join(s)
