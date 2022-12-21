class MyCircularQueue:

	def __init__(self, k: int):
		self.que = [None] * k
		self.que_maxlen = k
		self.p1 = 0
		self.p2 = 0

	def enQueue(self, value: int) -> bool:
		if self.que[self.p2] is None:
			self.que[self.p2] = value
			self.p2 = (self.p2 + 1) % self.que_maxlen
			return True
		else:
			return False

	def deQueue(self) -> bool:
		if self.que[self.p1] is None:
			return False
		else:
			self.que[self.p1] = None
			self.p1 = (self.p1 + 1) % self.que_maxlen
			return True

	def Front(self) -> int:
		return -1 if self.que[self.p1] is None else self.que[self.p1]

	def Rear(self) -> int:
		return -1 if self.que[self.p2 - 1] is None else self.que[self.p2 - 1]

	def isEmpty(self) -> bool:
		return self.p1 == self.p2 and self.que[self.p2] is None

	def isFull(self) -> bool:
		return self.p1 == self.p2 and self.que[self.p2] is not None
