import heapq


class SeatManager:

	def __init__(self, n: int):
		self.empty = []
		self.index = 0

	def reserve(self) -> int:
		if self.empty:
			seat = heapq.heappop(self.empty)
			return seat
		else:
			self.index += 1
			return self.index

	def unreserve(self, seatNumber: int) -> None:
		if seatNumber < self.index:
			heapq.heappush(self.empty, seatNumber)
		else:
			self.index -= 1

"""
리스트 만들어서 하면 TLE 뜸
*TESTCASE: 예외 범위 없음
"""