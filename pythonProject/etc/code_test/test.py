class Solution:
	def solution(self, code, message):
		code_list = [0]
		for i in code:
			code_list.append(i)

		if message.isdigit():
			msg_list = list(map(''.join, zip(*[iter(message)] * 2)))
			msg_list_check = []
			for msg in msg_list:
				msg_list_check.append(int(msg.lstrip('0')))
			answer = ""
			for i in msg_list_check:
				answer += code_list[i]

			return answer
		else:
			msg_list = []
			answer = ""
			for i in message:
				msg_list.append(i)
			print(msg_list)
			for i in msg_list:
				index = code_list.index(i)
				if index < 10:
					answer += str(index).zfill(2)
				else:
					answer += str(index)

			return answer

if __name__ == '__main__':
	sol = Solution()
	# a = sol.solution("abcdefghijklmnopqrstuvwxyz", "20051920"
	# print(a)

	b = sol.solution("abcdefghijklmnopqrstuvwxyz", "test")
	print(b)

# 2022-04-17
