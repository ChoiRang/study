def solution(citations):
	citations.sort(reverse=True)
	for idx, citation in enumerate(citations):
		if idx >= citation:
			return idx
	return len(citations)


# Programmers top1
def solution2(citations):
	citations.sort(reverse=True)
	answer = max(map(min, enumerate(citations, start=1)))
	return answer

if __name__ == '__main__':
	print(solution([3, 0, 6, 1, 5]))  # 3, 6->0, 5->1, 3->2, 1->3, 0->4
	print(solution([10, 10, 10, 10, 10]))  # 9=5
	print(solution([0, 0, 0, 0, 0]))  # 16=0
