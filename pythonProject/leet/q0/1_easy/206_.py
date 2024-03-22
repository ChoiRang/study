from typing import *


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		vals = []
		while head:
			vals.append(head.val)
			head = head.next
		i = len(vals) - 1
		root = node = ListNode(0)
		while i >= 0:
			node.next = ListNode(vals[i])
			node = node.next
			i -= 1

		return root.next
