import collections
from typing import *


class Solution:
	def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
		bidir_graph = collections.defaultdict(list)
		for i, j in edges:
			bidir_graph[i].append(j)
			bidir_graph[j].append(i)

		one_dir_node = []
		for i in bidir_graph:
			if len(bidir_graph[i]) == 1:
				one_dir_node.append(i)

		while n > 2:
			n -= len(one_dir_node)
			new_node = []
			for node in one_dir_node:
				p = bidir_graph[node].pop()
				bidir_graph[p].remove(node)

				if len(bidir_graph[p]) == 1:
					new_node.append(p)

			one_dir_node = new_node

		return one_dir_node
