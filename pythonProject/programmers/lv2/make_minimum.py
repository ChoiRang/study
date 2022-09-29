def solution(A, B):
	A_sort = sorted(A)
	B_sort = list(reversed(sorted(B)))
	mul_list = [a * b for a, b in zip(A_sort, B_sort)]
	return sum(mul_list)


if __name__ == '__main__':
	print(solution([1, 4, 2], [5, 4, 4]))
	print(solution([1, 2], [3, 4]))
