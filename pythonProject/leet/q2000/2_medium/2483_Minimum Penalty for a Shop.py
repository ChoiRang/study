class Solution:
	def bestClosingTime(self, customers: str) -> int:
		p_max = p = 0
		best = - 1
		for i, c in enumerate(customers):
			p += 1 if c == "Y" else -1
			if p > p_max:
				p_max, best = p, i
		return best + 1
