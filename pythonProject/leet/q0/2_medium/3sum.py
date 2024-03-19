from itertools import combinations
from collections import defaultdict
from typing import *


# !timeout! (140ms)
class Solution1:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums.sort()
		output = defaultdict(list)

		for i in combinations(nums, 3):
			output[sum(i)].append(i)

		result = output[0]

		return set(result)


# 3066ms 17.6mb
class Solution2:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums.sort()
		result = []

		for i in range(len(nums) - 2):
			if i > 0 and nums[i] == nums[i - 1]:
				continue
			left, right = i + 1, len(nums) - 1
			while left < right:
				sum_num = nums[i] + nums[left] + nums[right]
				if sum_num < 0:
					left += 1
				elif sum_num > 0:
					right -= 1
				else:
					result.append((nums[i], nums[left], nums[right]))
					left += 1
					right -= 1

		return set(result)


# ref, 3116ms 18.1mb
class Solution3:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums.sort()
		result = []

		for i in range(len(nums) - 2):
			if i > 0 and nums[i] == nums[i - 1]:
				continue
			left, right = i + 1, len(nums) - 1
			while left < right:
				sum_num = nums[i] + nums[left] + nums[right]
				if sum_num < 0:
					left += 1
				elif sum_num > 0:
					right -= 1
				else:
					result.append([nums[i], nums[left], nums[right]])

					while left < right and nums[left] == nums[left + 1]:
						left += 1
					while left < right and nums[right] == nums[right - 1]:
						right -= 1
					left += 1
					right -= 1

		return result