# 3124, 595 ms
def solution2(s):
	N = len(s)
	if N == 1:
		return 1
	answer = 0
	for i in range(0, N - 1):
		for j in range(i + 1, N + 1):
			pa = s[i:j]
			if len(pa) < answer:
				continue
			if pa == pa[::-1]:
				answer = max(answer, len(pa))

	return answer

# 느림! 3114, 3287 ms
def solution1(s):
	N = len(s)
	if N == 1:
		return 1
	answer = 0
	for i in range(0, N - 1):
		for j in range(i + 1, N + 1):
			pa = s[i:j]
			if pa == pa[::-1]:
				answer = max(answer, len(pa))

	return answer