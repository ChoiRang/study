def two_sum(nums, target):
	for i in range(len(nums) - 1):
		for j in range(i + 1, len(nums)):
			if nums[i] + nums[j] == target:
				return [i, j]


# 시간복잡도 : O(N^2)
# 공간복잡도 : O(1)


def two_sum2(nums, target):
	for i, num in enumerate(nums):
		res = target - num
		if res in nums[i + 1::]:
			return [i, i + 1 + nums[i + 1::].index(res)]


# 시간복잡도 : O(N^2)
# 공간복잡도 : O(1)


def two_sum3(nums, target):
	dicts = {}
	for i, num in enumerate(nums):
		res = target - num
		if res in dicts:
			return [i, dicts[res]]
		dicts[num] = i


# 시간복잡도 : O(N) * O(1) = O(N)
# 공간복잡도 : O(N) dicts 객체를 만들기 때문