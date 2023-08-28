class Solution:
	def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
		remain = purchaseAmount % 10
		if remain < 5:
			purchaseAmount -= remain
		else:
			purchaseAmount += (10 - remain)

		return 100 - purchaseAmount
