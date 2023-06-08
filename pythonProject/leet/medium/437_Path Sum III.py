from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
		count = 0

		def dfs(node, total):
			nonlocal count
			if not node: return
			total += node.val
			if total == targetSum:
				count += 1

			dfs(node.left, total)
			dfs(node.right, total)

		def dfs2(node):
			if not node: return
			dfs(node, 0)
			dfs2(node.left)
			dfs2(node.right)

		dfs2(root)
		return count
