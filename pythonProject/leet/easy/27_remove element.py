from typing import *


class Solution:
	def remove_element(self, nums: List[int], val: int) -> int:
		count = 0
		for i in range(len(nums)):
			if nums[i] != val:
				nums[count] = nums[i]
				print(count, i)
				count += 1

		return count, nums


if __name__ == '__main__':
	sol = Solution()
	print(sol.remove_element([3,2,2,3], 3))
