import bisect
from typing import *


class Solution:
	def primeSubOperation(self, nums: List[int]) -> bool:
		prime_list = [1 for i in range(1001)]
		prime_list[1] = 0
		for i in range(2, int(1001 ** 0.5) + 1):
			if prime_list[i]:
				for j in range(i * i, 1001, i):
					prime_list[j] = 0
		primes = [idx for idx, num in enumerate(prime_list) if num == 1]
		prev = 0

		for i in range(len(nums) - 1):
			num = nums[i]
			idx = bisect.bisect(primes, num) - 1
			cur = num - primes[idx]
			while idx > 0 and cur <= prev:
				idx -= 1
				cur = num - primes[idx]
			if cur <= prev: return False
			else: prev = cur

		if prev >= nums[-1]:
			return False

		return True


"""
prime_list[1] = 0으로 하여 primes=[0,2,3,5,7...]으로 만듦
-> while 문에서 cur 값을 구할때 idx=1에서도 최소값이 안나올 경우 0을 빼게 함으로써 nums[i]가 최소임을 보증한다.
->? #if num(cur) > prev: pass 는 해당 num 값이 최소라는 보장이 없다.
"""
