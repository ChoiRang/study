from typing import *
import collections


# REF
class Solution2:
	def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
		intervals = collections.defaultdict(int)
		for start, end in flowers:
			intervals[start] += 1
			intervals[end + 1] -= 1

		blooming, count = {}, 0
		person = sorted(people, reverse=True)
		for time in sorted(intervals.keys()):
			change = intervals[time]
			while person and time > person[-1]:
				blooming[person.pop()] = count
			if not person:
				break
			count += change

		return [blooming[p] if p in blooming else 0 for p in people]


# MLE
class Solution:
	def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
		dp = [0] * (max(map(max, flowers)) + 2)
		for start, end in flowers:
			dp[start] += 1
			dp[end + 1] -= 1

		bloom = [0]
		for i in dp:
			bloom.append(bloom[-1] + i)
		n = len(bloom)

		res = []
		for p in people:
			if p < n:
				res.append(bloom[p + 1])
			else:
				res.append(0)

		return res
