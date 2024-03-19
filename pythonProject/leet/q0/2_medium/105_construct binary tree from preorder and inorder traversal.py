from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution1:
	def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
		"""
		preorder = root left right
		inorder = left root right
		"""
		if inorder:
			index = inorder.index(preorder.pop(0))
			print(index)

			node = TreeNode(inorder[index])
			node.left = self.buildTree(preorder, inorder[0:index])
			node.right = self.buildTree(preorder, inorder[index + 1:])

			return node


