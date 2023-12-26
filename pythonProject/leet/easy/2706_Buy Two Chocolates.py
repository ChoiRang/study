from typing import *


class Solution:
	def buyChoco(self, prices: List[int], money: int) -> int:
		res = money + 1
		n = len(prices)
		for i in range(n):
			for j in range(i + 1, n):
				price = prices[i] + prices[j]
				if price <= money and price < res:
					res = price

		return money if res > money else money - res
