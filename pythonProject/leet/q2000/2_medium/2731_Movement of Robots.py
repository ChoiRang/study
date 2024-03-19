from typing import *


class Solution:
	def sumDistance(self, nums: List[int], s: str, d: int) -> int:
		N = len(nums)
		MOD = 10 ** 9 + 7

		for idx, direction in enumerate(s):
			if direction == "L":
				nums[idx] -= d
			else:
				nums[idx] += d

		nums.sort()
		prev, total = 0, 0

		for i in range(N):
			total = (total + i * nums[i] - prev) % MOD
			prev += nums[i] % MOD

		return total % MOD


"""
1. 로봇이 충돌할경우 각자 반대방향으로 이동한다 -> 좌우 1칸씩 이동 -> 서로 통과하여 지나가는 효과
if idx=j => abs(nums[j]-nums[0] + nums[j]-nums[1] + ... + nums[j]-nums[j-1])
nums[i] < nums[j] => nums[j]-nums[0] + nums[j]-nums[1] + ... + nums[j]-nums[j-1]
nums[j]-nums[0] + nums[j]-nums[1] + ... + nums[j]-nums[j-1] => j*nums[j] - sum(nums[0]+ ... + nums[j-1])
j*nums[j] - sum(nums[0]+ ... + nums[j-1]) => i*nums[i] - prev
"""
