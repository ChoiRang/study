from typing import *


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		res = ListNode(0)
		res.next = head
		tmp, tmp2 = res, res
		for _ in range(n):
			tmp = tmp.next
		while tmp.next:
			tmp = tmp.next
			tmp2 = tmp2.next
		tmp2.next = tmp2.next.next
		return res.next
