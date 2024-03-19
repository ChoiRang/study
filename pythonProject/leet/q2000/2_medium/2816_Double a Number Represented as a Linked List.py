from typing import *


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
		root = head
		num = 0
		while root:
			num = num * 10 + root.val
			root = root.next

		num *= 2
		digit = []
		if num == 0:
			return ListNode(0)
		while num > 0:
			digit.append(num % 10)
			num //= 10

		start = ListNode()
		head = start
		for d in reversed(digit):
			head.next = ListNode(d)
			head = head.next

		return start.next
