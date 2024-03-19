from typing import *
import collections


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		counter = collections.Counter()

		def dfs(node, depth):
			if not node:
				return
			counter[depth] += node.val
			dfs(node.left, depth + 1)
			dfs(node.right, depth + 1)

		dfs(root, 0)

		def dfs1(node, depth, curr: Optional[TreeNode]):
			left, right = 0, 0
			if node.left: left = node.left.val
			if node.right: right = node.right.val
			total = counter[depth] - left - right
			if node.left:
				curr.left = TreeNode(total)
				dfs1(node.left, depth + 1, curr.left)
			if node.right:
				curr.right = TreeNode(total)
				dfs1(node.right, depth + 1, curr.right)

			return curr

		res = dfs1(root, 1, TreeNode(0))

		return res
