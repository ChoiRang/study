from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def __init__(self):
		self.max_dim = 0

	def dfs(self, node):
		if node is None:
			return 0

		left = self.dfs(node.left)
		right = self.dfs(node.right)
		self.max_dim = max(self.max_dim, left + right)
		return max(left, right) + 1

	def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
		self.dfs(root)
		return self.max_dim
