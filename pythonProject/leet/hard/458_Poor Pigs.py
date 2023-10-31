class Solution:
	def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
		limit = minutesToTest // minutesToDie
		i = 0

		while (limit + 1) ** i < buckets:
			i += 1

		return i


"""
테스트를 할 수 있는 기회가 limit번 있을 때 최적의 돼지 수를 찾아야 한다.

"""
