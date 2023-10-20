from typing import *
import collections

class Solution:
	def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
		graph = collections.defaultdict(list)
		for x, y in relations:
			graph[x].append(y)

		route_times = [0] * (n + 1)

		def calc_time(start):
			if route_times[start] > 0:
				return route_times[start]

			max_time = 0
			for dest in graph[start]:
				max_time = max(max_time, calc_time(dest))

			total = time[start - 1] + max_time
			route_times[start] = total
			return total

		res = 0
		for i in range(1, n + 1):
			res = max(res, calc_time(i))

		return res


"""
* route_times: (dp), 시작점에서의 결과를 저장하여 값이 있을경우 재귀 없이 바로 반환하게 한다. (중복 계산 방지)
"""
