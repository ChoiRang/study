# Definition for a binary tree node.
from typing import *


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def minDepth(self, root: Optional[TreeNode]) -> int:
		if root is None:
			return 0

		return self.dfs(root)

	def dfs(self, node):
		if node is None:
			return float('inf')

		if node.left is None and node.right is None:
			return 1

		return min(self.dfs(node.left), self.dfs(node.right)) + 1
