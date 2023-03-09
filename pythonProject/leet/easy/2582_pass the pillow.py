class Solution:
	def passThePillow(self, n: int, time: int) -> int:
		if (time // (n - 1)) % 2 == 0:
			return 1 + time % (n - 1)
		else:
			return n - time % (n - 1)

"""
n=4, time=5
234 -> 321 -> 234 순으로 반복 (3 배수 만큼 반복)
time // (n-1) -> 5 // 3 = 1 홀수로 감소하고 있는 중
n - time%(n-1) -> 4 - 2 = 2

n=4, time=2
time // (n-1) -> 2 // 3 = 0 짝수로 증가세
1 + time%(n-1) -> 1 + 2 = 3
(n-1)? -> 3만큼 반복
1 + , n - ? -> 상승 및 하강의 숫자 단위가 그 이전 단계의 마지막 숫자부터 시작
"""
