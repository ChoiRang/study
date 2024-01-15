max_num = int(input())
num_list = [int(input()) for _ in range(max_num)]

if max_num == 1:
	print(num_list[0])
elif max_num == 2:
	print(num_list[0]+num_list[1])
else:
	step = [num_list[0], num_list[0]+num_list[1]]
	step.append(max(num_list[0]+num_list[2], num_list[1]+num_list[2]))

	for i in range(3, max_num):
		step.append(max(num_list[i]+num_list[i-1]+step[i-3], num_list[i]+step[i-2]))

	print(step[-1])
