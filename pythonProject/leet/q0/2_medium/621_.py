import collections
from typing import *


class Solution:
	def leastInterval(self, tasks: List[str], n: int) -> int:
		counter = collections.Counter(tasks)
		max_count = max(counter.values())
		max_count_tasks = sum(1 for count in counter.values() if count == max_count)
		interval_length = (max_count - 1) * (n + 1) + max_count_tasks

		return max(len(tasks), interval_length)


"""
max_count -> 가장 많은 알파벳 갯수
max_count_tasks -> 최대값이 같은 알파벳 갯수
모든 알파벳을 동일한 갯수만큼 가지고 있을때 결과는 tasks 의 길이다.
이런 경우가 아닐경우, max_count 만큼 interval을 무조건 돌아야 한다. 다시 돌아오는 시간은 쿨링 시간 (n+1) 포함하며 마지막 순회 전까지 계산하면
-> (max_count - 1) * (n + 1)
위 식은 <"A", "B", ..."B", "C" > 즉, 마지막 "A" 전까지 다시 돌아온 상태이다. (다른 알파벳이 얼만큼 있든 상관없이 무조건 걸리는 시간임) 이후 남은 알파벳을 순회하면 (max_count_tasks)
-> (max_count - 1) * (n + 1) + max_count_tasks
특정 알파벳이 다른 알파벳보다 많을때의 경우의 수 계산이다.
"""
