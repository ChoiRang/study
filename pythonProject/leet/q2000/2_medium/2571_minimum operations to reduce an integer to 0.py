import bisect


class Solution:
	def minOperations(self, n: int) -> int:
		power_2 = [2 ** i for i in range(20)]
		count = 0

		while n != 0:
			point = bisect.bisect(power_2, abs(n)) - 1
			left, right = abs(n - power_2[point]), abs(n - power_2[point + 1])
			if left <= right:
				n -= power_2[point]
			else:
				n = power_2[point + 1] - n
			count += 1

		return count


"""
0이 되는 항상 최선의 경로를 찾아야 함

"""