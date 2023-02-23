from typing import *
import collections


class Solution:
	def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
		bi_route = collections.defaultdict(list)
		visit = set()

		for x, y in edges:
			bi_route[x].append(y)
			bi_route[y].append(x)

		def dfs(node, visit):
			if node == destination:
				return True
			visit.add(node)
			for i in bi_route[node]:
				if i not in visit and dfs(i, visit):
					return True

			return False

		return dfs(source, visit)
