# Definition for a Node.
class Node:
	def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
		self.val = int(x)
		self.next = next
		self.random = random


class Solution:
	def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
		if not head:
			return None

		node_list = {}

		curr = head
		while curr:
			node_list[curr] = Node(curr.val)
			curr = curr.next

		curr = head
		while curr:
			node_list[curr].next = node_list.get(curr.next)
			node_list[curr].random = node_list.get(curr.random)
			curr = curr.next

		return node_list[head]
