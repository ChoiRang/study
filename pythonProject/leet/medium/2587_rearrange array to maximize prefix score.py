class Solution:
	def maxScore(self, nums: List[int]) -> int:
		nums.sort(reverse=True)
		result = 0
		prefix = [0]
		for num in nums:
			prefix.append(prefix[-1] + num)

		for i in range(1, len(prefix)):
			if prefix[i] > 0:
				result = i

		return result


# REF
class Solution:
	def maxScore(self, nums: List[int]) -> int:
		ans = len(nums)
		ss = sum(nums)

		heapq.heapify(nums)
		while nums and ss <= 0:
			ss -= heapq.heappop(nums)
			ans -= 1
		return ans