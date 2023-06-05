from typing import *


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def pairSum(self, head: Optional[ListNode]) -> int:
		p1, p2 = head, head
		max_sum = 0
		while p2 and p2.next:
			p1 = p1.next
			p2 = p2.next.next

		curr, prev = p1, None
		while curr:
			curr.next, curr, prev, = prev, curr.next, curr

		while prev:
			max_sum = max(max_sum, prev.val + head.val)
			prev, head = prev.next, head.next

		return max_sum
