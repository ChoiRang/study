class Solution:
	def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
		dist = 0
		while mainTank >= 5:
			mainTank -= 5
			dist += 5
			if additionalTank >= 1:
				mainTank += 1
				additionalTank -= 1

		dist += mainTank
		return dist * 10


class Solution2:
	def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
		return (mainTank + min((mainTank - 1) // 4, additionalTank)) * 10
