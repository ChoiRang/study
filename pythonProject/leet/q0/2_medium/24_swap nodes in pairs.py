from typing import *


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
		root = prev = ListNode(0)
		prev.next = head

		while head and head.next:
			listnode_1 = head.next
			head.next = listnode_1.next
			listnode_1.next = head

			prev.next = listnode_1

			head = head.next
			prev = prev.next.next
		return root.next