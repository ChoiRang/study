import collections
from typing import List


class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		courses = collections.defaultdict(list)
		visited = set()
		traced = set()

		for a, b in prerequisites:
			courses[a].append(b)

		for a in list(courses):
			if not self.dfs(a, courses, traced, visited):
				return False

		return True

	def dfs(self, a: int, courses, traced, visited):
		if a in traced:
			return False
		if a in visited:
			return True

		traced.add(a)
		for b in courses[a]:
			if not self.dfs(b, courses, traced, visited):
				return False
		traced.remove(a)
		visited.add(a)

		return True
