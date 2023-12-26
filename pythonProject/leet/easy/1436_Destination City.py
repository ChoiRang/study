class Solution:
	def destCity(self, paths: List[List[str]]) -> str:
		graph = set()
		for start, _ in paths:
			graph.add(start)

		for _, end in paths:
			if end not in graph:
				return end

		return ""