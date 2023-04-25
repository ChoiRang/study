class Solution:
	def sumOfMultiples(self, n: int) -> int:
		count = 0
		divisible = [3, 5, 7]
		for i in range(1, n + 1):
			for divis in divisible:
				if i % divis == 0:
					count += i
					break

		return count

# REF
class Solution2:
	def sumOfMultiples2(self, n: int) -> int:
		ret = 0

		for num in range(1, n + 1):
			if num % 3 == 0 or num % 5 == 0 or num % 7 == 0: ret += num

		return ret
