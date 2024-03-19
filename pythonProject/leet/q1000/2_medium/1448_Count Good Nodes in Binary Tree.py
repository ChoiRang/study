from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def __init__(self):
		self.count = 0

	def goodNodes(self, root: TreeNode) -> int:
		def dfs(node, now):
			if node:
				if node.val >= now:
					self.count += 1
					now = node.val
				dfs(node.left, now)
				dfs(node.right, now)

		dfs(root, -10 ** 4)
		return self.count
