class Solution:
	def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
		total = numOnes + numZeros
		if total >= k:
			return min(numOnes, k)
		else:
			return numOnes - (k - total)
