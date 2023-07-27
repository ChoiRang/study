from typing import *


class Solution:
	def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
		n = len(positions)
		sorted_idx = sorted(range(n), key=lambda i: positions[i])
		left, right = [], []
		for i in sorted_idx:
			curr_hp = healths[i]
			if directions[i] == "R":
				right.append([i, curr_hp])
			else:
				while right and right[-1][1] < curr_hp:
					right.pop()
					curr_hp -= 1

				if right and right[-1][1] == curr_hp:
					right.pop()
					curr_hp = 0
				elif right and 0 < curr_hp < right[-1][1]:
					right[-1][1] -= 1
					curr_hp = 0
g
				if curr_hp:
					left.append([i, curr_hp])
		res = left + right
		res.sort()

		return [x[1] for x in res]
