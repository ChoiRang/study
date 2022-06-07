def solution(number):
	answer = []
	while number:
		if number % 3:
			answer.append(str(number % 3))
			number //= 3
		else:
			answer.append('4')
			number = number // 3 - 1
	return ''.join(reversed(answer))


if __name__ == '__main__':
	print(solution(1))
	print(solution(2))
	print(solution(3))
	print(solution(4))
	print(solution(5))
	print(solution(6))
	print(solution(7))
	print(solution(8))
	print(solution(9))
	print(solution(10))
	print(solution(50))
