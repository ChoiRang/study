from typing import *
import heapq


class Graph2:
	def __init__(self, n: int, edges: List[List[int]]):
		self.n = n
		self.graph = [[] for _ in range(n + 1)]

		for start, end, dist in edges:
			self.graph[start].append((end, dist))

	def addEdge(self, edge: List[int]) -> None:
		self.graph[edge[0]].append((edge[1], edge[2]))

	def shortestPath(self, node1: int, node2: int) -> int:
		INF = 10 ** 7
		heap = []
		best = [INF] * self.n
		heapq.heappush(heap, (0, node1))

		while len(heap) > 0:
			dist, start = heapq.heappop(heap)
			if start == node2:
				return dist

			for dest, dest_dist in self.graph[start]:
				if best[dest] > dist + dest_dist:
					best[dest] = dist + dest_dist
					heapq.heappush(heap, (dist + dest_dist, dest))

		return -1


class Graph:
	def __init__(self, n: int, edges: List[List[int]]):
		self.edges = n
		self.my_graph = {i: [] for i in range(n)}
		for start, end, dist in edges:
			self.my_graph[start].append([end, dist])

	def addEdge(self, edge: List[int]) -> None:
		self.my_graph[edge[0]].append([edge[1], edge[2]])

	def shortestPath(self, node1: int, node2: int) -> int:
		INF = 10 ** 9
		heap = [(0, node1)]
		total_dist = {i: INF for i in range(self.edges)}
		while heap:
			dist, start = heapq.heappop(heap)
			if start == node2:
				return dist
			if dist > total_dist[start]:
				continue
			for end, dist2 in self.my_graph[start]:
				new_dist = dist + dist2
				if new_dist < total_dist[end]:
					total_dist[end] = new_dist
					heapq.heappush(heap, (new_dist, end))

		return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
"""
단방향 그래프 및 목적지 까지의 최소값 거리 요구 -> heap 사용(자동 정렬)
"""
