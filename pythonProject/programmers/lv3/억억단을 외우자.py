def solution(e, starts):
	nums = [0 for _ in range(e + 1)]
	for i in range(1, e + 1):
		for j in range(i, e + 1):
			if i * j > e: break
			if i == j:
				nums[i * j] += 1
			else:
				nums[i * j] += 2

	res = [0 for _ in range(e + 1)]
	max_val = 0
	for i in range(e, 0, -1):
		if nums[i] >= max_val:
			max_val = nums[i]
			res[i] = i
		else:
			res[i] = res[i + 1]

	return [res[start] for start in starts]

"""
약수 구하고 -> 역순으로 큰 숫자 변경되는 지점 감지
i==j 기준으로 양쪽의 결과값이 같음
리스트 역순으로 최대값을 확인 -> 같거나 크면 작은 인덱스가 정답이므로 갱신
"""