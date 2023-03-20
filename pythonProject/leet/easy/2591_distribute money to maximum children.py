class Solution:
	def distMoney(self, money: int, children: int) -> int:
		count = 0
		money -= children
		if money < 0:
			return -1
		for i in range(children):
			if money < 7:
				break
			elif i == children - 2 and money == 10:
				break
			elif i == children - 1 and money > 7:
				break
			money -= 7
			count += 1

		return count

