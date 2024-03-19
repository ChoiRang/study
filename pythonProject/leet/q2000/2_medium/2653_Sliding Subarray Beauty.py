from sortedcontainers import SortedList
from typing import *


class Solution2:
	def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
		N = len(nums)
		res = []
		sort_list = SortedList() # 외부 라이브러리임
		for i in range(N):
			sort_list.add(nums[i])
			if i >= k:
				sort_list.remove(nums[i - k])
			if len(sort_list) == k:
				res.append(min(0, sort_list[x - 1]))

		return res


# TLE
class Solution1:
	def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
		N = len(nums)
		res = []
		for i in range(N - k + 1):
			num = sorted(nums[i:i + k])[x - 1]
			if num < 0:
				res.append(num)
			else:
				res.append(0)

		return res


# REF, 가장 빠른 방법
class Solution3:
	def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
		lis = list(range(-50, 1))
		count = {n: 0 for n in lis}
		for i in range(k):
			if nums[i] <= 0:
				count[nums[i]] += 1
			else:
				count[0] += 1
		ans = []
		rest = 0
		for n in lis:
			rest += count[n]
			if rest >= x:
				ans.append(n)
				break
		# print([(n,count[n]) for n in lis if count[n] > 0],ans,rest)
		for i in range(k, len(nums)):
			a, b = nums[i], nums[i - k]
			if a > 0:
				a = 0
			if b > 0:
				b = 0
			if b <= ans[-1]:
				rest -= 1
			if a <= ans[-1]:
				rest += 1
			count[b] -= 1
			count[a] += 1
			temp = ans[-1]
			if rest < x:
				while rest < x:
					temp += 1
					rest += count[temp]
			elif rest >= x + count[temp]:
				while rest >= x + count[temp]:
					rest -= count[temp]
					temp -= 1
			ans.append(temp)
		# print([(n,count[n]) for n in lis if count[n] > 0],ans,rest)
		return ans
