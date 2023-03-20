import collections
import itertools
import math
from functools import cache
from typing import List


# REF
@cache
def primeFactors(n):
	ans = {}
	while n % 2 == 0:
		ans[2] = ans.get(2, 0) + 1
		n = n // 2

	for i in range(3, 6, 2):
		while n % i == 0:
			ans[i] = ans.get(i, 0) + 1
			n = n // i

	if n > 2:
		ans[n] = 1
	return ans


class Solution5:
	def findValidSplit(self, nums: List[int]) -> int:
		n = len(nums)
		if n == 1: return -1

		pfs = [primeFactors(x) for x in nums]

		last_occurence = {}

		i = n - 1
		while i >= 0:
			pf = pfs[i]
			for k in pf.keys():
				if k not in last_occurence:
					last_occurence[k] = i
			i -= 1

		ans = 0
		for i in range(n):
			pf = pfs[i]
			for k in pf.keys():
				ans = max(ans, last_occurence[k])

			if ans == i: return ans
			if ans == n - 1: return -1
		return -1


class Solution4:
	def findValidSplit(self, nums: List[int]) -> int:
		primes = collections.Counter()
		lines = [0 for _ in range(len(nums))]
		for idx, num in enumerate(nums):
			for p in self.get_prime(num):
				if p not in primes:
					primes[p] = idx
				lines[primes[p]] += 1
				lines[idx] -= 1
		sum = 0
		for i in range(len(nums) - 1):
			sum += lines[i]
			if sum == 0:
				return i

		return -1

	def get_prime(self, n: int) -> list[int]:
		res = []
		if n % 2 == 0:
			res.append(2)
			while n % 2 == 0:
				n /= 2
		if n % 3 == 0:
			res.append(3)
			while n % 3 == 0:
				n /= 3
		i = 6
		while i < 1000 and n > 1:
			i1, i2 = i - 1, i + 1
			if n % i1 == 0:
				res.append(i1)
				while n % i1 == 0:
					n /= i1
			if n % i2 == 0:
				res.append(i2)
				while n % i2 == 0:
					n /= i2
			i += 6
		if n > 1:
			res.append(n)
		return res


# TLE (10000 -list)
# 2의 소수 찿는 부분 list->Counter 로 변경
class Solution3:
	def findValidSplit(self, nums: List[int]) -> int:
		primes = collections.Counter()
		for i in range(len(nums)):
			x = nums[i]
			j = 2
			while j <= math.sqrt(x):
				while x % j == 0:
					primes[j] += 1
					x //= j
				j += 1
			if x > 1:
				primes[x] += 1

		prefix = collections.Counter()
		overlap = collections.Counter()

		for i in range(len(nums) - 1):
			x = nums[i]
			j = 2
			while j <= math.sqrt(x):
				while x % j == 0:
					x //= j
					prefix[j] += 1
					primes[j] -= 1
					overlap[j] = min(prefix[j], primes[j])
					if overlap[j] == 0:
						del overlap[j]
				j += 1
			if x > 1:
				prefix[x] += 1
				primes[x] -= 1
				overlap[x] = min(prefix[x], primes[x])
				if overlap[x] == 0:
					del overlap[x]
			if len(overlap) == 0:
				return i

		return -1


# TLE
class Solution2:
	def findValidSplit(self, nums: List[int]) -> int:
		if len(nums) == 2: return 0
		fc_list = self.factorize(nums)

		for i in range(len(nums) - 2):
			skip = False
			list1 = set(itertools.chain(*fc_list[:i + 1]))
			list2 = set(itertools.chain(*fc_list[i + 1:]))
			for val in list1:
				if val in list2:
					skip = True
					continue
			if not skip:
				return i

		return -1

	def factorize(self, nums):
		result = []
		for num in nums:
			factor = 2
			factors = set()
			while factor ** 2 <= num:
				while num % factor == 0:
					factors.add(factor)
					num = num // factor
				factor += 1
			if num > 1:
				factors.add(num)
			result.append(factors)
		return result


# REF
# def gcd(self, x, y):
#     if x % y == 0:
#         return y
#     elif y == 0:
#         return x
#     else:
#         return gcd(y, x % y)


# TLE
class Solution1:
	def findValidSplit(self, nums: List[int]) -> int:
		if len(nums) == 2: return 0
		for i in range(len(nums) - 2):
			if math.gcd(math.prod(nums[:i + 1]), math.prod(nums[i + 1:])) == 1:
				return i

		return -1
