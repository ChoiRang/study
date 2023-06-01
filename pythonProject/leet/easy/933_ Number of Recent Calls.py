import collections


class RecentCounter:

	def __init__(self):
		self.times = collections.deque()

	def ping(self, t: int) -> int:
		print("t:", t)
		self.times.append(t)

		while t - self.times[0] > 3000:
			self.times.popleft()

		return len(self.times)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
