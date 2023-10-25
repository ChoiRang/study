from typing import *
import collections


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def largestValues(self, root: Optional[TreeNode]) -> List[int]:
		count = collections.defaultdict(list)

		def dfs(node, depth):
			if node:
				count[depth].append(node.val)
				dfs(node.left, depth + 1)
				dfs(node.right, depth + 1)

		dfs(root, 0)

		res = []
		for key in count.keys():
			res.append(max(count[key]))

		return res
