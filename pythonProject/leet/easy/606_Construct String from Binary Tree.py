from typing import *


# Definition for a binary tree node.

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def tree2str(self, root: Optional[TreeNode]) -> str:
		def dfs(node):
			res = ""
			if node.left:
				res = "(" + str(node.left.val) + dfs(node.left) + ")"
			if node.right:
				if res:
					res += "(" + str(node.right.val) + dfs(node.right) + ")"
				else:
					res = "()(" + str(node.right.val) + dfs(node.right) + ")"

			return res

		return str(root.val) + dfs(root)
