# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	value = 0

	def bstToGst(self, root: TreeNode) -> TreeNode:
		def dfs(node):
			if node:
				node.right = dfs(node.right)
				self.value += node.val
				node.val = self.value
				node.left = dfs(node.left)

			return node

		return dfs(root)
