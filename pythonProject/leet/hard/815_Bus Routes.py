from typing import *
import collections


class Solution:
	def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
		if source == target:
			return 0

		bus_st = collections.defaultdict(set)

		for idx, locations in enumerate(routes):
			for dest in locations:
				bus_st[dest].add(idx)

		deque = collections.deque(bus_st[target])
		res = 0
		visited = set()

		while deque:
			res += 1
			for _ in range(len(deque)):
				from_st = deque.popleft()
				visited.add(from_st)
				if source in routes[from_st]:
					return res
				for loc in routes[from_st]:
					for bus in bus_st[loc]:
						if bus not in visited:
							deque.append(bus)

		return -1
