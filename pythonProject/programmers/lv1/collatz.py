def solution(num):
	count = 0

	while True:
		if num == 1:
			return count

		num = num/2 if num % 2 == 0 else (num*3)+1
		count += 1

		if count == 500:
			return -1


if __name__ == '__main__':
    print(solution(626331))
