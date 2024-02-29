import collections
import unittest
from typing import *


def check(word: str):
	n = len(word)
	i = 0
	seen = set()
	while i < n:
		ch = word[i]
		if ch in seen:
			return False
		seen.add(ch)
		while i < n and word[i] == ch:
			i += 1

	return True


def solutions(words: List[str]) -> str:
	# ==========
	# n = int(input())
	# words = [input() for _ in range(n)]
	# ==========
	words = collections.deque(words)
	for word in words:
		if not check(word):
			return "gg"
	for ch in [chr(x) for x in range(97, 123)]:
		front_ch, all_ch, rear_ch = [], [], []
		for _ in range(len(words)):
			word = words.popleft()
			if word[0] == word[-1] == ch:
				all_ch.append(word)
			elif word[0] == ch:
				front_ch.append(word)
			elif word[-1] == ch:
				rear_ch.append(word)
			else:
				words.append(word)
		if not (front_ch or all_ch or rear_ch):
			continue
		if len(front_ch) > 1 or len(rear_ch) > 1:
			return "gg"

		curr_str = ""
		if rear_ch:
			curr_str = rear_ch[0]
		for st in all_ch:
			curr_str += st
		if front_ch:
			curr_str += front_ch[0]
		if not check(curr_str):
			return "gg"
		words.append(curr_str)

	total = ""
	for _ in range(len(words)):
		word = words.popleft()
		total += word
		words.append(word)

	if not check(total):
		return "gg"
	if len(words) > 1: return "-_-"

	return words.popleft()


class Test(unittest.TestCase):
	def test1(self):
		self.assertEqual(solutions(["te", "st"]), "stte")

	def test2(self):
		self.assertEqual(solutions(["aaa", "a", "aa"]), "aaaaaa")

	def test3(self):
		self.assertEqual(solutions(["ab", "bba"]), "gg")

	def test4(self):
		self.assertEqual(solutions(["te", "s", "t"]), "-_-")

	def test5(self):
		self.assertEqual(solutions(["orr", "rd", "woo", "www"]), "wwwwooorrrd")

	def test6(self):
		self.assertEqual(solutions(["abcb"]), "gg")

	def test7(self):
		self.assertEqual(solutions(["abcd", "dddde"]), "abcddddde")

	def test8(self):
		self.assertEqual(solutions(["abcd", "dddde", "ffffa"]), "ffffaabcddddde")

	def test9(self):
		self.assertEqual(solutions(["abcd", "dbca"]), "gg")

	def test10(self):
		self.assertEqual(solutions(["abcd", "deee", "ffffa"]), "ffffaabcddeee")

	def test11(self):
		self.assertEqual(solutions(["abcd", "deee", "ffffa", "eeaa"]), "gg")

	def test12(self):
		self.assertEqual(solutions(["ab", "bc", "cd", "cccc"]), "abbccccccd")

	def test13(self):
		self.assertEqual(solutions(["sss", "aassbb"]), "gg")
