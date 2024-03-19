from typing import *
import collections


class Solution:
	def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
		degree = [0] * n
		for x in leftChild + rightChild:
			if x != -1:
				degree[x] += 1

		root = None
		for i in range(n):
			if degree[i] == 0:
				if root is None:
					root = i
				else:
					return False
		if root is None:
			return False

		visited = [False] * n
		que = collections.deque([root])

		while que:
			node = que.popleft()
			if visited[node]:
				return False
			visited[node] = True
			if leftChild[node] != -1:
				que.append(leftChild[node])
			if rightChild[node] != -1:
				que.append(rightChild[node])

		return sum(visited) == n
