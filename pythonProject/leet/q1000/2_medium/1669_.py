# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
		head = list1

		for _ in range(a - 1):
			list1 = list1.next

		tmp = list1
		for _ in range(b - a + 1):
			tmp = tmp.next

		list1.next = list2
		while list1.next:
			list1 = list1.next

		list1.next = tmp.next

		return head
