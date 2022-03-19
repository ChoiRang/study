# [1차] 비밀지도


def solution(n, arr1, arr2):
	answer = []

	def length_cut(bin_number1, bin_number2, n):
		bin_num1 = bin_number1[2:]
		bin_num2 = bin_number2[2:]
		bin_len1 = len(bin_num1)
		bin_len2 = len(bin_num2)

		if bin_len1 < n:
			for i in range(n-bin_len1):
				bin_num1 = '0' + bin_num1
			bin_len1 = n
		if bin_len2 < n:
			for i in range(n-bin_len2):
				bin_num2 = '0' + bin_num2
			bin_len2 = n

		if bin_len1 > bin_len2:
			for i in range(bin_len1-bin_len2):
				bin_num2 = '0' + bin_num2
		elif bin_len1 < bin_len2:
			for i in range(bin_len2-bin_len1):
				bin_num1 = '0' + bin_num1

		return bin_num1, bin_num2

	for i in range(n):
		bin_num1 = bin(arr1[i])
		bin_num2 = bin(arr2[i])
		num1, num2 = length_cut(bin_num1, bin_num2, n)
		output = ''
		for j in range(n):
			if num1[j] == '0' and num2[j] == '0':
				output += ' '
			else:
				output += '#'
		answer.append(output)

	return answer


if __name__ == '__main__':
	n_ = 6
	arr1_ = [46, 33, 33, 22, 31, 50]
	arr2_ = [27, 56, 19, 14, 14, 10]
	print(solution(n_, arr1_, arr2_))
