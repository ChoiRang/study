import collections


class Solution2:
	def isFascinating(self, n: int) -> bool:
		s = str(n) + str(n * 2) + str(n * 3)
		if "0" in s:
			return False
		check = set()
		for ch in s:
			if ch in check:
				return False
			check.add(ch)
		return True


class Solution1:
	def isFascinating(self, n: int) -> bool:
		nums = collections.Counter()
		for i in range(1, 4):
			val = n * i
			print(val)
			for j in str(val):
				nums[j] += 1
		if nums["0"]: return False
		for i in nums.values():
			if i > 1:
				return False
		return True
