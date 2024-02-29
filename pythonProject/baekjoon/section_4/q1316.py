import unittest
from typing import *


def solutions(words: List[str]) -> int:
	# ==========
	# n = int(input())
	# words = [input() for _ in range(n)]
	# ==========
	n = len(words)
	# ==========
	res = n
	for i in range(n):
		seen = set()
		prev = ""
		for ch in words[i]:
			if ch in seen:
				res -= 1
				break
			if prev != ch:
				seen.add(prev)
			prev = ch
	return res


class Test(unittest.TestCase):
	def test1(self):
		self.assertEqual(solutions(["happy", "new", "year"]), 3)

	def test2(self):
		self.assertEqual(solutions(["aba", "abab", "abcabc", "a"]), 1)

	def test3(self):
		self.assertEqual(solutions(["ab", "aa", "aca", "ba", "bb"]), 4)

	def test4(self):
		self.assertEqual(solutions(["yzyzy", "zyzyz"]), 0)

	def test5(self):
		self.assertEqual(solutions(["z"]), 1)

	def test6(self):
		self.assertEqual(solutions(["aaa", "aaazbz", "babb", "aazz", "azbz", "aabbaa", "abacc", "aba", "zzaz"]), 2)

	def test7(self):
		self.assertEqual(solutions(["abcd"]), 1)
