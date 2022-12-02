class Solution:
	def myAtoi(self, s: str) -> int:
		INT_MIN = -(2 ** 31)
		INT_MAX = (2 ** 31) - 1
		int_s = []
		s = s.lstrip()
		sign = 1
		if len(s) == 0:
			return 0

		if s[0] == '+' or s[0] == '-':
			if s[0] == '-':
				sign = -1
			for ch in s[1:]:
				if ch.isdigit():
					int_s.append(ch)
				else:
					break
		else:
			for ch in s:
				if ch.isdigit():
					int_s.append(ch)
				else:
					break

		if not int_s:
			return 0

		# min, max diff
		answer = int(('').join(int_s)) * sign
		if answer < INT_MIN:
			return INT_MIN
		elif answer > INT_MAX:
			return INT_MAX
		else:
			return answer