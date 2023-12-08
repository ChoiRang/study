class Solution:
	def totalMoney(self, n: int) -> int:
		week, day = divmod(n, 7)
		res = 28 * week
		for i in range((week + 1), week + day + 1):
			res += i
		for i in range(1, week):
			res += 7 * i
		return res
