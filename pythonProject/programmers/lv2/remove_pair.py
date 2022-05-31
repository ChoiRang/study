def solution(s):
	new_str = []
	for i in range(len(s)):
		if not new_str:
			new_str.append(s[i])
		else:
			if s[i] == new_str[-1]:
				new_str.pop()
			else:
				new_str.append(s[i])
	if not new_str:
		return 1
	else:
		return 0


if __name__ == '__main__':
	print(solution('baabaa'))		# 1
	print(solution('cdcddc'))		# 0
	print(solution('cdd'))			# 0
	print(solution('abbaeea'))		# 0
	print(solution('abccbaee'))		# 1
