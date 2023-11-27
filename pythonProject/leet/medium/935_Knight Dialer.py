class Solution:
	def knightDialer(self, n: int) -> int:
		MOD = 10 ** 9 + 7
		res = [1 for _ in range(10)]
		for i in range(n - 1):
			dp = [
				res[4] + res[6],
				res[6] + res[8],
				res[7] + res[9],
				res[4] + res[8],
				res[3] + res[9] + res[0],
				0,
				res[1] + res[7] + res[0],
				res[2] + res[6],
				res[1] + res[3],
				res[2] + res[4]
			]
			res = dp

		return sum(res) % MOD


"""
나이트는 n-1 번 점프를 할 수 있다.
나이트는 숫자판 어디에서든지 시작할 수 있다.

--> 숫자판 5를 제외한 어디에서 시작하든 점프가 가능하다, 5번으로 가지 않는다.
모든 점프는 각
"""