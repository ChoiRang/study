from sortedcontainers import SortedSet
from typing import *
import collections


class FoodRatings:

	def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
		self.foods = {}
		self.cuisines = collections.defaultdict(SortedSet)
		for i in range(len(foods)):
			self.foods[foods[i]] = (cuisines[i], ratings[i])
			self.cuisines[cuisines[i]].add((-ratings[i], foods[i]))

	def changeRating(self, food: str, newRating: int) -> None:
		cuisine, rate = self.foods[food]
		self.foods[food] = (cuisine, newRating)
		self.cuisines[cuisine].remove((-rate, food))
		self.cuisines[cuisine].add((-newRating, food))

	def highestRated(self, cuisine: str) -> str:
		return self.cuisines[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
