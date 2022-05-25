def solution(arr):
	if len(arr) > 1:
		arr.remove(min(arr))
		return arr
	else:
		return [-1]


if __name__ == '__main__':
	print(solution([10]))
	print(solution([4, 3, 2, 1]))


