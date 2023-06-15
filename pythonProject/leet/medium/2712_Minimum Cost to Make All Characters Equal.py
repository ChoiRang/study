class Solution:
	def minimumCost(self, s: str) -> int:
		n = len(s)
		s = [int(i) for i in s]
		start = n // 2
		res = []
		odd = (n % 2 == 1)
		for num in range(2):
			if odd: num = s[start]

			count = 0
			left_invert, right_invert = False, False

			for i in range(odd, start + odd):
				left, right = start - i - (not odd), start + i
				if left_invert:
					if num == s[left]:
						left_invert = False
						count += (left + 1)
				else:
					if num != s[left]:
						left_invert = True
						count += (left + 1)
				if right_invert:
					if num == s[right]:
						right_invert = False
						count += (n - right)
				else:
					if num != s[right]:
						right_invert = True
						count += (n - right)
			res.append(count)
			if odd: break

		return min(res)
