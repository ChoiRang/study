# REF
class Solution2:
	def minimumOneBitOperations(self, n: int) -> int:
		res = 0
		while n:
			res ^= n
			n >>= 1
		return res


class Solution:
	def minimumOneBitOperations(self, n: int) -> int:
		n = bin(n)[2:]
		ex = len(n)
		res = 0
		p = 1

		for i in range(len(n)):
			if n[i] == "1":
				res += p * (2 ** ex - 1)
				p *= -1
			ex -= 1

		return res


"""
n의 비트를 전부 0으로 만들기
1. 0번째(가장 우측) 변경 가능
2. i-1 == 1, i-2 부터~ == 0 일때 i 변경 가능
-> 1000~ 을 만들어야 함
	ex)	110100
    	543210 = idx
    	op2 => i-1 = 1, i-2 0~ 은 idx 3부분만 있다.
    	op1 => idx=0 은 항상 바꿀 수 있다.
	ex)	11010 -> 11011 -> 11001 -> 11000 -> 01000
						-> 01001 -> 01011 -> 01010 -> 01110
						-> 01111 -> 01101 -> 01100 -> 00100
						-> 00101 -> 00111 -> 00110 -> 00010
						-> 00011 -> 00001 -> 00000
	* 1000 -> 15 steps -> 2^4 - 1
	* 100 ->  7 steps -> 2^3 - 1
	* 10 -> 3 steps -> 2^2 -1
	1010 = 2^4-1 - 2^2-1
	11010 = 2^5-1 - 2^4-1 + 2^2-1
	=> res = val1-(val2-(val3-(val4-val5))) = val1 - val2 + val3 - val4 + val5
"""
