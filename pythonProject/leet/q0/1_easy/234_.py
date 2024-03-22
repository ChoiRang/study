from typing import *


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def isPalindrome(self, head: Optional[ListNode]) -> bool:
		fast = head
		vals = []
		while fast and fast.next:
			vals.append(head.val)
			head = head.next
			fast = fast.next.next
		if fast: head = head.next
		i = -1
		while head:
			if vals[i] != head.val:
				return False
			i -= 1
			head = head.next

		return True
