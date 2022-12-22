class MyCircularDeque:
	"""
	slow! (isEmpty() -> O(n))
	"""
	def __init__(self, k: int):
		self.que = [None] * k
		self.que_len, self.que_maxlen = 0, k
		self.p1, self.p2 = 0, 0

	def insertFront(self, value: int) -> bool:
		print('insert before:', self.que, self.p1)
		if self.que[self.p1] is None:
			self.que[self.p1] = value
			return True
		elif self.que[self.p1] is not None:
			print(self.p1)
			p1_before = self.p1
			self.p1 = (self.p1 - 1) % self.que_maxlen
			print(self.p1)
			if self.que[self.p1] is None:
				self.que[self.p1] = value
				return True
			else:
				self.p1 = p1_before
				return False
		else:
			return False

	def insertLast(self, value: int) -> bool:
		if self.que[self.p2] is None:
			self.que[self.p2] = value
			return True
		elif self.que[self.p2] is not None:
			p2_before = self.p2
			self.p2 = (self.p2 + 1) % self.que_maxlen
			if self.que[self.p2] is None:
				self.que[self.p2] = value
				return True
			else:
				self.p2 = p2_before
				return False
		else:
			return False

	def deleteFront(self) -> bool:
		if self.que[self.p1] is not None:
			self.que[self.p1] = None
			if not self.isEmpty():
				self.p1 = (self.p1 + 1) % self.que_maxlen
			return True
		else:
			return False

	def deleteLast(self) -> bool:
		print('delete before:', self.que)
		if self.que[self.p2] is not None:
			self.que[self.p2] = None
			if not self.isEmpty():
				self.p2 = (self.p2 - 1) % self.que_maxlen
			return True
		else:
			return False

	def getFront(self) -> int:
		if self.que[self.p1] is not None:
			return self.que[self.p1]
		else:
			return -1

	def getRear(self) -> int:
		if self.que[self.p2] is not None:
			return self.que[self.p2]
		else:
			return -1

	def isEmpty(self) -> bool:
		for i in self.que:
			if i is not None:
				return False
		return True

	def isFull(self) -> bool:
		for i in self.que:
			if i is None:
				return False
		return True


# ref
class MyCircularDeque2:
	def __init__(self, k: int):
		# self.sz = 0
		self.data = []
		self.K = k

	def insertFront(self, value: int) -> bool:
		if len(self.data) == self.K:
			return False
		else:
			self.data[0:0] = [value]
			print(self.data)
			return True

	def insertLast(self, value: int) -> bool:
		if len(self.data) == self.K:
			return False
		else:
			self.data.append(value)
			return True

	def deleteFront(self) -> bool:
		if len(self.data) == 0:
			return False
		else:
			self.data.pop(0)
			return True

	def deleteLast(self) -> bool:
		if len(self.data) == 0:
			return False
		else:
			self.data.pop()
			return True

	def getFront(self) -> int:
		if len(self.data) == 0:
			return -1
		else:
			return self.data[0]

	def getRear(self) -> int:
		if len(self.data) == 0:
			return -1
		else:
			return self.data[-1]

	def isEmpty(self) -> bool:
		return len(self.data) == 0

	def isFull(self) -> bool:
		return len(self.data) >= self.K