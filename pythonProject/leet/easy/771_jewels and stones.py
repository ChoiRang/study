class Solution:
	def numJewelsInStones(self, jewels: str, stones: str) -> int:
		count_stone = dict()
		total = 0
		for stone in stones:
			if stone in count_stone.keys():
				count_stone[stone] += 1
			else:
				count_stone[stone] = 1

		for jewel in jewels:
			if jewel in count_stone:
				total += count_stone[jewel]

		return total
