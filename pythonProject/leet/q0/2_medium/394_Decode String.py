class Solution:
	def decodeString(self, s: str) -> str:
		stack = []
		cur_num, cur_str = 0, ""
		for i, ch in enumerate(s):
			if ch == '[':
				stack.append(cur_str)
				stack.append(cur_num)
				cur_str = ""
				cur_num = 0
			elif ch == ']':
				num = stack.pop()
				prev_str = stack.pop()
				cur_str = prev_str + num * cur_str
			elif ch.isdigit():
				cur_num = cur_num * 10 + int(ch)
			else:
				cur_str += ch

		return cur_str
