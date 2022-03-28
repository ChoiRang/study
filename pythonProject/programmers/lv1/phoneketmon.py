def solution(nums):
	num_len_half = len(nums) / 2
	set_nums = set(nums)
	set_len = len(set_nums)
	if set_len >= num_len_half:
		return num_len_half
	else:
		return set_len


if __name__ == '__main__':
	nums = [3, 1, 2, 3]
	print(solution(nums))

