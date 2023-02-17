class Solution:
	def reverse(self, x: int) -> int:
		is_minus = (x < 0)
		result = 0
		if is_minus:
			x *= -1
		digit_count = 0

		while x > 0:
			result *= 10
			result += x % 10
			x //= 10

		if is_minus:
			result *= -1
		if -2 ** 31 <= result <= 2 ** 31 - 1:
			return result

		return 0
