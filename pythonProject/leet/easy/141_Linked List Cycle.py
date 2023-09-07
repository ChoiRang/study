from typing import *


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def hasCycle(self, head: Optional[ListNode]) -> bool:
		slow = head
		while head and head.next:
			slow = slow.next
			head = head.next.next
			if slow == head:
				return True

		return False


"""
pos 가 매개변수로 주어지지 않음, pos= -1 -> False
* 링크드 리스트에 사이클이 있는지 묻는 여부
"""
