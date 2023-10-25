class Solution:
	def kthGrammar(self, n: int, k: int) -> int:
		if n == 1:
			return 0
		prev = 1 << (n - 2)

		if k <= prev:
			return self.kthGrammar(n - 1, k)
		else:
			return 0 if self.kthGrammar(n - 1, k - prev) == 1 else 1


"""
n 만큼 반복하면서 0 -> 01, 1->10 으로 변환함. 즉 2배수씩 늘어남
(1-indexed)
n=1, 0
n=2, 01
n=3, 0110
n=4, 01101001
중간을 기점으로 완벽한 반대값이 뒤로 추가되는 패턴이다.
k의 값이 뭔지는 몰라도, 절반 기준으로 값이 항상 반대값이다 => k가 절반보다 크면 값을 뒤집어야 한다.
n=4,k=6-4=2 ->	역 (k=6 prev=4)
n=3 k=2      		(k=2 <= prev=2)
n=2 k=2-1=1 -> 	역 (k=2 prev=1)
n=1 에서 값이 0 반환, 과정을 역으로 올라가면 답은 0 -> 1 -> 1 -> 0
"""
