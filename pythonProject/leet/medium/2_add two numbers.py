from typing import *


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


# len(1) -> Error - Found cycle in the ListNode
class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		root = head = ListNode(0)
		tens = 0

		while l1 or l2:
			sum_num = 0
			if l1:
				sum_num += l1.val
				l1 = l1.next
			if l2:
				sum_num += l2.val
				l2 = l2.next

			tens, remain = divmod(sum_num + tens, 10)

			head.next = ListNode(remain)
			head = head.next

		if tens == 1:
			head.next = ListNode(1)

		return root.next