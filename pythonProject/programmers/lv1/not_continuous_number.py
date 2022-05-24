# 같은 숫자는 싫어
def solution(arr):
	answer = [number for index, number in enumerate(arr) if not (index > 0 and arr[index-1] == number)]
	return answer


if __name__ == '__main__':
	print(solution([1,1,3,3,0,1,1]))
	print(solution([4,4,4,3,3]))