from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


# check!
class Solution:
	def longestZigZag(self, root: Optional[TreeNode]) -> int:
		total = 0

		def dfs(node, flag, total):
			if not node:
				return total - 1

			left = dfs(node.left, 0, total + 1 if flag else 1)
			right = dfs(node.right, 1, total + 1 if not flag else 1)

			return max(left, right)

		return dfs(root, None, 0)
1