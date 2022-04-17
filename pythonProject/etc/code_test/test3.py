class Solution:
	def solution(self, candles):
		day = 1
		while day <= len(candles):
			candles.sort(reverse=True)
			for i in range(day):
				candles[i] -= 1
				if candles[i] == -1:
					return day - 1
			day += 1
		return day - 1


if __name__ == '__main__':
	sol = Solution()
	print(sol.solution([5, 2, 2, 1]))
	print(sol.solution([1, 2, 3, 4, 5, 6]))

# 2022-04-17

