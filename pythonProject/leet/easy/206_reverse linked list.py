from typing import *


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
		if left == right:
			return head

		root = start = ListNode()
		root.next = head

		for _ in range(left - 1):
			start = start.next

		end = start.next
		for _ in range(right - left):
			tmp, start.next, end.next = start.next, end.next, end.next.next
			start.next.next = tmp

		return root.next
