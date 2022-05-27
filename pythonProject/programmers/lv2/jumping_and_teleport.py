def solution(n):
	jump_count = 0
	while n != 0:
		if n % 2 == 0:
			n /= 2
		else:
			n -= 1
			jump_count += 1
	return jump_count


if __name__ == '__main__':
	print(solution(5))
	print(solution(6))
	print(solution(5000))


