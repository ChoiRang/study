# slow, more memory
class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		table = {
			')': '(',
			']': '[',
			'}': '{'
		}

		for ch in s:
			if ch not in table:
				stack.append(ch)
			elif not stack or table[ch] != stack.pop():
				return False

		return len(stack) == 0
