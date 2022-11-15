def solution(a, b, n):
	get_cola = []
	while n >= a:
		n, remain = divmod(n, a)
		n *= b
		get_cola.append(n)
		n += remain
	return sum(get_cola)


if __name__ == '__main__':
	print(solution(2, 1, 20))  # 19
	print(solution(3, 1, 20))  # 9
	print(solution(3, 2, 20))  # 36
