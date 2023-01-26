from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


# 결과 값 이진 트리가 높이 차이가 1 이하여야 함
class Solution:
	def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
		if not nums:
			return None

		mid = len(nums) // 2

		node = TreeNode(nums[mid])
		node.left = self.sortedArrayToBST(nums[:mid])
		node.right = self.sortedArrayToBST(nums[mid + 1:])

		return node


# ref
class Solution2:
	def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
		def dfs(left, right):
			if left > right:
				return None

			mid = (left + right) // 2
			node = TreeNode(nums[mid])
			node.left = dfs(left, mid - 1)
			node.right = dfs(mid + 1, right)

			return node

		return dfs(0, len(nums) - 1)

# return dfs(0, len(nums)) -> index out of range
