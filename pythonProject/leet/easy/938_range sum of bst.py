from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	result = 0

	def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
		def dfs(node):
			if node is None:
				return None

			value = node.val
			if low <= value <= high:
				self.result += value

			node.left = dfs(node.left)
			node.right = dfs(node.right)

			return node

		dfs(root)
		return self.result
