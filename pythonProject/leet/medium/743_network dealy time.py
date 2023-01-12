import collections
import heapq
from typing import List


class Solution:
	def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
		graph = collections.defaultdict(list)

		for start, end, time in times:
			graph[start].append((end, time))

		dist = {}
		heap = []
		heapq.heappush(heap, (0, k))

		while heap:
			total_time, start = heapq.heappop(heap)
			if start not in dist:
				dist[start] = total_time
				for end, time in graph[start]:
					heapq.heappush(heap, (total_time + time, end))

		print(dist)
		if len(dist) == n:
			return max(dist.values())

		return -1
