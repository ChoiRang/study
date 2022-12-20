import collections


class MyStack:

	def __init__(self):
		self.que = collections.deque()

	def push(self, x: int) -> None:
		self.que.append(x)
		for _ in range(len(self.que) - 1):
			self.que.append(self.que.popleft())

	def pop(self) -> int:
		return self.que.popleft()

	def top(self) -> int:
		return self.que[0]

	def empty(self) -> bool:
		return len(self.que) == 0
