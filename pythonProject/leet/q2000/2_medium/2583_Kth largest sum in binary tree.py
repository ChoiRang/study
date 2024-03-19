from typing import *
import collections


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
		total = collections.defaultdict(int)

		def dfs(node, depth):
			if node is None:
				return None
			if total[depth]:
				total[depth] += node.val
			else:
				total[depth] = node.val

			dfs(node.left, depth + 1)
			dfs(node.right, depth + 1)

		dfs(root, 0)

		return -1 if len(total.values()) < k else sorted(total.values(), reverse=True)[k - 1]
