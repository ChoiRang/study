import unittest
import re


def solutions2(code):
	p = re.compile('(100+1+|01)+')
	if p.fullmatch(code):
		return "YES"
	else:
		return "NO"


# 왜 안됨?
def solutions(code: str):
	i = 0
	n = len(code)
	print(n)
	str_code = ""
	while i < n:
		str_code += code[i]
		if len(str_code) == 2 and str_code == "01":
			str_code = ""
			i += 1
		elif len(str_code) == 3 and str_code == "100":
			while i < n and code[i] == "0":
				i += 1
			if i >= n:
				return "NO"

			prev_i = i
			while i < n and code[i] == "1":
				i += 1
			str_code = ""
			if n-1 > i > prev_i+1 and code[i] == "0" and code[i+1] == "0":
				i -= 1
		else:
			i += 1
	return "YES" if len(str_code) == 0 else "NO"


class Test(unittest.TestCase):
	def test1(self):
		self.assertEqual(solutions("10010111"), "NO")

	def test2(self):
		self.assertEqual(solutions("011000100110001"), "NO")

	def test3(self):
		self.assertEqual(solutions("0110001011001"), "YES")

	def test4(self):
		self.assertEqual(solutions("1001"), "YES")

	def test5(self):
		self.assertEqual(solutions("10010"), "NO")

	def test6(self):
		self.assertEqual(solutions("1010"), "NO")

	def test7(self):
		self.assertEqual(solutions("10000000000111111111111111"), "YES")

	def test8(self):
		self.assertEqual(solutions("1001100001"), "YES")

	def test9(self):
		self.assertEqual(solutions("10000011111111100"), "NO")

	def test10(self):
		self.assertEqual(solutions("100000111111111001"), "YES")

	def test11(self):
		self.assertEqual(solutions("1001100101"), "YES")

	def test12(self):
		self.assertEqual(solutions("100110011101"), "YES")

	def test13(self):
		self.assertEqual(solutions("100110011101010101"), "YES")

	def test14(self):
		self.assertEqual(solutions("1001100110"), "NO")

	def test15(self):
		self.assertEqual(solutions("10000"), "NO")

	def test16(self):
		self.assertEqual(solutions("01100111011"), "NO")

	def test17(self):
		self.assertEqual(solutions("100101011"), "NO")

	def test18(self):
		self.assertEqual(solutions("1001100011100111000001"), "YES")

	def test19(self):
		self.assertEqual(solutions("10100101"), "NO")

	def test20(self):
		self.assertEqual(solutions("100100"), "NO")


	def test_imsi(self):
		self.assertEqual(solutions("10001110001"), "YES")
