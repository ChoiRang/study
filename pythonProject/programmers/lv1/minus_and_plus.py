def solution(absolutes, signs):
	max_size = len(absolutes)
	for i in range(max_size):
		if signs[i] is False:
			absolutes[i] = absolutes[i] * -1

	return sum(absolutes)

def solution2(absolutes, signs):
	pass

if __name__ == '__main__':
	print(solution([4, 7, 12], [True, False, True]))
