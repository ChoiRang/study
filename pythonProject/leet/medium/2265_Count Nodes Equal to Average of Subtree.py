from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
		self.res = 0
		head = root

		def post_order(node):
			if node is None:
				return 0, 0

			left, left_count = post_order(node.left)
			right, right_count = post_order(node.right)

			curr_sum = node.val + left + right
			curr_count = left_count + right_count + 1

			if curr_sum // curr_count == node.val:
				self.res += 1
			return curr_sum, curr_count

		post_order(root)
		return self.res
