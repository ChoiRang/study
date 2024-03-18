# Definition for singly-linked list.
from typing import *


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
		root = ListNode(0)
		root.next = head
		prefix = {0: root}
		prefix_sum = 0
		while head:
			prefix_sum += head.val
			if prefix_sum in prefix:
				prev = prefix[prefix_sum]
				node = prev.next
				p = prefix_sum + (node.val if node else 0)
				while p != prefix_sum:
					del prefix[p]
					node = node.next
					p += node.val if node else 0
				prev.next = head.next
			else:
				prefix[prefix_sum] = head
			head = head.next
		return root.next
