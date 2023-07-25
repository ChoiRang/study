from typing import *


class Solution:
	def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
		res = [0] * len(queries)
		server = {i: 0 for i in range(1, n + 1)}
		logs.sort(key=lambda x: (x[1], x[0]))
		queries = sorted([query, i] for i, query in enumerate(queries))
		left, right = 0, 0
		count = n
		for query, i in queries:
			while right < len(logs) and logs[right][1] <= query:
				server_id = logs[right][0]
				if server[server_id] == 0:
					count -= 1
				server[server_id] += 1
				right += 1
			while left < len(logs) and logs[left][1] < query - x:
				server_id = logs[left][0]
				server[server_id] -= 1
				if server[server_id] == 0:
					count += 1
				left += 1
			res[i] = count

		return res
