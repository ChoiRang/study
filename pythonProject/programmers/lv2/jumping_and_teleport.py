def solution(n):		# 시간초과.. ?
	jump_count = 1
	while n > 2:
		if n % 2 == 1:
			jump_count += 1
			n -= 1
		n /= 2
	return jump_count


def solution2(n):		# note
	return bin(n)[2:].count('1')


if __name__ == '__main__':
	print(solution(5))
	print(solution(6))
	print(solution(5000))
