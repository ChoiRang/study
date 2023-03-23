import math
from typing import *


class Solution:
	def repairCars(self, ranks: List[int], cars: int) -> int:
		low, high = 0, max(ranks) * cars ** 2

		def time_check(time):
			finish = 0
			for rank in ranks:
				finish += int(math.sqrt(time / rank))
			return finish >= cars

		while low < high:
			mid = (high + low) // 2

			if time_check(mid):
				high = mid
			else:
				low = mid + 1

		return low

"""
모든 차를 수리하는대 필요한 최소 시간(차량 수리 시간중 제일 긴시간)
수리시간 -> r * n * n = time  =>  n = sqrt(time/r), n:차량
수리 시간: 0 ~ max(ranks)* cars ** 2 사이
시간 기준으로 모든 n(차량)을 구하여 더한 값(finish)이 총 차량 갯수(cars)이상이면 기준 시간이 크게 잡힌 경우로, high = mid
작으면 low = mid+1
"""
