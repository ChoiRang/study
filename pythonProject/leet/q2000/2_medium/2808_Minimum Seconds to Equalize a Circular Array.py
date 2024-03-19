from typing import *
import collections
import copy


class Solution3:
	def minimumSeconds(self, nums: List[int]) -> int:
		n = len(nums)
		dist = collections.defaultdict(list)

		for i, num in enumerate(nums):
			dist[num].append(i)

		res = n
		for key in dist.keys():
			key_len = len(dist[key])
			if key_len != 1:
				max_dist = dist[key][0] + n - dist[key][-1]
				for i in range(key_len - 1):
					max_dist = max(max_dist, (dist[key][i + 1] - dist[key][i]) )

				res = min(res, max_dist)

		return res // 2

"""
같은 수 사이의 거리 // 2 만큼이 최소 시간
dist[key][0] + n - dist[key][-1] -> 처음과 끝부분의 보정 거리
"""


# TLE
class Solution2:
	def __init__(self):
		self.N = 0
		self.change = []

	def minimumSeconds(self, nums: List[int]) -> int:
		n = len(nums)
		res = []
		for i in range(n):
			self.change.append([(i - 1 + n) % n, (i + 1) % n])
		self.N = len(self.change)
		count = collections.Counter(nums)
		_, total = count.most_common(1)[0]

		for num, num_count in count.most_common():
			deep_nums = copy.deepcopy(nums)
			res.append(self.check(num, num_count, deep_nums))

		return min(res)

	def check(self, num, num_have, nums):
		res = 0
		n = len(nums)
		count = num_have
		while count < n:
			res += 1
			idxs = []
			for i in range(self.N):
				prev, come = self.change[i]
				if nums[i] == num:
					idxs.append(prev)
					idxs.append(come)
			for i in idxs:
				if nums[i] != num:
					nums[i] = num
					count += 1

		return res


# 리스트 참조 문제, 리스트의 기본 총합이 기준 숫자의 총합보다 더 큰 문제(or [3, 6, 9]처럼 같은 문제)
class Solution1:
	def minimumSeconds(self, nums: List[int]) -> int:
		n = len(nums)
		res = 0
		change = []
		for i in range(n):
			change.append([(i - 1 + n) % n, (i + 1) % n])

		count = collections.Counter(nums)
		num, total = count.most_common(1)[0]

		while total < n:
			res += 1
			for i in range(n):
				prev, come = change[i]
				if nums[prev] == num:
					count[nums[i]] -= 1
					count[num] += 1
				elif nums[come] == num:
					count[nums[i]] -= 1
					count[num] += 1
			num, total = count.most_common(1)[0]

		return res
