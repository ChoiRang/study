class Solution:
	def minOperations(self, s: str) -> int:
		def get_min(start):
			res = 0
			for i, num in enumerate(s):
				if i % 2 == 0 and start != num:
					res += 1
				elif i % 2 == 1 and start == num:
					res += 1
			return res

		return min(get_min("0"), get_min("1"))
