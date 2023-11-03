from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def findMode(self, root: Optional[TreeNode]) -> List[int]:
		best = []
		best_count, curr_node, curr_count = 0, root, 0

		def in_order(node):
			if node is None:
				return
			in_order(node.left)

			nonlocal best
			nonlocal best_count, curr_node, curr_count

			if curr_node.val == node.val:
				curr_count += 1
			else:
				curr_node = node
				curr_count = 1

			if curr_count > best_count:
				best = [curr_node.val]
				best_count = curr_count
			elif curr_count == best_count:
				best.append(curr_node.val)
			in_order(node.right)

		in_order(root)
		return best

"""
inorder 좌 -> 루트 -> 우

"""