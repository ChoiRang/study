import collections


def solution(tickets):
	tickets = sorted(tickets, key=lambda x: x[1], reverse=True)
	route = collections.defaultdict(list)
	stack = ['ICN']
	path = []
	for start, end in tickets:
		route[start].append(end)

	while stack:
		next = stack.pop()
		if route[next]:
			stack.append(next)
			stack.append(route[next].pop())
		else:
			path.append(next)

	return path[::-1]
