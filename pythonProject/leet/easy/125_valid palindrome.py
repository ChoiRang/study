import re


class Solution:
	# noinspection PyMethodMayBeStatic
	def is_palindrome(self, s: str) -> bool:
		st = re.sub('[^a-z0-9]', '', s.lower())
		return st == st[::-1]


if __name__ == '__main__':
	sol = Solution()
	print(sol.is_palindrome("A man, a plan, a canal: Panama"))
	print(sol.is_palindrome("race a car"))
	print(sol.is_palindrome(" "))
