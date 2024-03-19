import collections


# REF
class Solution2:
	def minDeletions(self, s: str) -> int:
		res = 0
		counter = collections.Counter(s)
		seen = set()
		for i in counter.values():
			while i in seen and i > 0:
				res += 1
				i -= 1
			seen.add(i)

		return res
	"무엇을 빼든 1개만 존재하면 되기에 순서가 필요하지 않음"


class Solution1:
	def minDeletions(self, s: str) -> int:
		res = 0
		counter = collections.Counter(s)
		dp = [0] * (max(counter.values()))
		n = len(dp)
		for i in counter.values():
			dp[i - 1] += 1
		change = True

		while change:
			change = False
			for i in range(n):
				if i > 0 and dp[i] > 1:
					dp[i - 1] += 1
					dp[i] -= 1
					res += 1
					change = True
				elif dp[i] > 1:
					dp[i] -= 1
					res += 1
					change = True

		return res
