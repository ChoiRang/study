from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
		def dfs(node, leaf: List):
			if node.left is None and node.right is None:
				leaf.append(node.val)

			if node.left:
				dfs(node.left, leaf)
			if node.right:
				dfs(node.right, leaf)
			return leaf

		return dfs(root1, []) == dfs(root2, [])
