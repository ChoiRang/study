class Solution:
	def alternateDigitSum(self, n: int) -> int:
		count = 0
		result = 0
		n_list = [int(i) for i in str(n)]
		for num in n_list:
			if count % 2 == 0:
				result += num
			else:
				result -= num
			count += 1

		return result
