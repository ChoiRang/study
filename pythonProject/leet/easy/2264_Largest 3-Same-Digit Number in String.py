class Solution:
	def largestGoodInteger(self, num: str) -> str:
		prev = ""
		count = 0
		res = ""
		for ch in num:
			if ch == prev:
				count += 1
			else:
				count = 1
				prev = ch
			if count == 3:
				res = max(res, prev)

		return res * 3
