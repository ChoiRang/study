import heapq


def dijkstra(dist, path):
	heap = []
	heapq.heappush(heap, [1, 0])
	while heap:
		node, total_distance = heapq.heappop(heap)
		for end, distance in path[node]:
			if total_distance + distance < dist[end]:
				dist[end] = total_distance + distance
				heapq.heappush(heap, [end, total_distance + distance])

	return dist


def solution(N, road, K):
	each_dist = [float('inf') for _ in range(N+1)]
	each_dist[1] = 0
	path = [[] for _ in range(N+1)]
	for i in road:
		start, end, distance = i
		path[start].append([end, distance])
		path[end].append([start, distance])
	print(path)
	dist = dijkstra(each_dist, path)
	print(dist)
	return len([i for i in dist if i <= K])


if __name__ == '__main__':
	print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)) # 4
