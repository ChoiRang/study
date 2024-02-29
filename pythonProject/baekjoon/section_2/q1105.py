import unittest


def solution(l, r) -> int:
	# l ,r = map(str, input().split())
	l, r = str(l), str(r)
	if len(l) != len(r):
		return 0
	res = 0
	for i in range(len(l)):
		if l[i] == r[i]:
			if l[i] == "8":
				res += 1
		else:
			break
	return res


class Test(unittest.TestCase):
	def test1(self):
		self.assertEqual(solution(1, 10), 0)

	def test2(self):
		self.assertEqual(solution(88, 88), 2)

	def test3(self):
		self.assertEqual(solution(800, 899), 1)

	def test4(self):
		self.assertEqual(solution(8808, 8880), 2)

	def test5(self):
		self.assertEqual(solution(78, 88), 0)

	def test6(self):
		self.assertEqual(solution(1, 882), 0)

	def test7(self):
		self.assertEqual(solution(88, 881), 0)

	def test8(self):
		self.assertEqual(solution(8888888, 8888890), 5)
