class Solution:
	def numberOfMatches(self, n: int) -> int:
		res = 0
		while n > 1:
			odd = n % 2 == 1
			n //= 2
			res += n
			if odd:
				n += 1

		return res
