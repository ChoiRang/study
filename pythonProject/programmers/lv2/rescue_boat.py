# 구명 보트
from collections import deque


def solution(people, limit):
	people_deque = deque(sorted(people))
	answer = 0

	while people_deque:
		if len(people_deque) == 1:
			answer += 1
			break
		if people_deque[0] + people_deque[-1] <= limit:
			people_deque.pop()
			people_deque.popleft()
		else:
			people_deque.pop()
		answer += 1

	return answer


# people_deque[0] 기준으로 [-1] 번째와의 합이 imit 보다 작아질 때까지 큰수를 제거
if __name__ == '__main__':
	print(solution([70, 50, 80, 50], 100))
	print(solution([70, 80, 50], 100))
	print(solution([30, 40, 50, 60], 100))
