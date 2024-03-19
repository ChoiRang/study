from typing import *
import math


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
		res = root = head
		prev_val = head.val
		head = head.next
		while head:
			gcd = math.gcd(prev_val, head.val)
			node = ListNode(gcd)
			node.next = ListNode(head.val)

			root.next = node
			root = root.next.next

			prev_val = head.val
			head = head.next

		return res
