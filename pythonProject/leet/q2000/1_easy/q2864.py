class Solution:
	def maximumOddBinaryNumber(self, s: str) -> str:
		count = s.count("1")
		print(count)
		res = ""
		for i in range(len(s) - 1):
			if count > 1:
				res += "1"
				count -= 1
			else:
				res += "0"

		return res + "1"
