def solution(n):
	n_case = [1, 1]
	if n == 1:
		return 1
	for i in range(2, n+1):
		n_case.append(n_case[i-2]+n_case[i-1])
	return n_case[n] % 1234567


if __name__ == '__main__':
	print(solution(1))
	print(solution(2))
	print(solution(3))
	print(solution(4))
	print(solution(5))
	# 피보나치 수열, 1, 2, 3, 5, 8, 13 ...
