import collections


# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Codec:
	def serialize(self, root: TreeNode) -> str:
		"""
		Encodes a tree to a single string.
		"""
		depth_count = dict()
		result = []

		def check(node):
			if node is None:
				result.append(1001)
				return

			result.append(node.val)
			check(node.left)
			check(node.right)

		check(root)

		return ','.join(map(str, result))

	def deserialize(self, data: str) -> TreeNode:
		"""
		Decodes your encoded data to tree.
		"""

		data = collections.deque(map(int, data.split(',')))
		print(data)

		def get_node():
			x = int(data.popleft())
			if x > 1000:
				return None

			node = TreeNode(x)
			node.left = get_node()
			node.right = get_node()
			return node

		result = get_node()
		return result

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
