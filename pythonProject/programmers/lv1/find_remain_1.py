def solution(n):
	for i in range(1, n):
		if n % i == 1:
			return i


def solution2(n):
	return [i for i in range(1, n) if n % i == 1][0]


if __name__ == '__main__':
	print(solution(10))
	print(solution2(12))
