import collections


class Solution:
	def isItPossible(self, word1: str, word2: str) -> bool:
		w1 = collections.Counter(word1)
		w2 = collections.Counter(word2)
		print("www")
		print(w1, w2)
		for x in list(w1.keys()):
			for y in list(w2.keys()):
				w1[x] -= 1
				w1[y] += 1
				w2[x] += 1
				w2[y] -= 1

				if w1[x] == 0:
					del w1[x]
				if w2[y] == 0:
					del w2[y]

				if len(w1) == len(w2):
					return True

				w1[x] += 1
				w1[y] -= 1
				w2[x] -= 1
				w2[y] += 1

				if w1[y] == 0:
					del w1[y]
				if w2[x] == 0:
					del w2[x]

		return False
