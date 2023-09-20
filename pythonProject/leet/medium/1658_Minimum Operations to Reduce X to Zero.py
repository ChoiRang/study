class Solution:
	def minOperations(self, nums: List[int], x: int) -> int:
		total = sum(nums)
		target = total - x

		if target < 0:
			return -1

		if target == 0:
			return len(nums)

		n = len(nums)
		res, curr = n + 1, 0
		left, right = 0, 0
		while right < n:
			curr += nums[right]
			right += 1
			while curr > target and left < right:
				curr -= nums[left]
				left += 1

			if curr == target:
				res = min(res, n - (right - left))

		return -1 if res > n else res


