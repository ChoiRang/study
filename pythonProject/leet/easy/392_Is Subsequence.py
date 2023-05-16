import collections


class Solution1:
	def isSubsequence(self, s: str, t: str) -> bool:
		deq = collections.deque(s)
		pt = 0

		while deq:
			if pt == len(t):
				return False

			if deq[0] == t[pt]:
				deq.popleft()
			pt += 1

		return True
