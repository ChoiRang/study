class Solution:
	def isPathCrossing(self, path: str) -> bool:
		visited = set()
		x, y = 0, 0
		visited.add((0, 0))
		for d in path:
			if d == "N":
				y += 1
			elif d == "S":
				y -= 1
			elif d == "E":
				x += 1
			else:
				x -= 1
			if (x, y) in visited:
				return True
			visited.add((x, y))

		return False
