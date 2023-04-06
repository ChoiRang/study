def solution(board, skill):
	tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
	R, C = len(board[0]), len(board)
	for type, r1, c1, r2, c2, degree in skill:
		if type == 1: degree *= -1
		tmp[r1][c1] += degree
		tmp[r1][c2 + 1] += -degree
		tmp[r2 + 1][c1] += -degree
		tmp[r2 + 1][c2 + 1] += degree

	for i in range(C):
		for j in range(R):
			tmp[i][j + 1] += tmp[i][j]
	for j in range(R):
		for i in range(C):
			tmp[i + 1][j] += tmp[i][j]
	count = 0
	for i in range(C):
		for j in range(R):
			if board[i][j] + tmp[i][j] > 0:
				count += 1

	return count