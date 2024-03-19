class Solution:
	def removeDuplicateLetters(self, s: str) -> str:
		duple_last = dict()
		stack = []
		visited = set()

		for idx, ch in enumerate(s):
			duple_last[ch] = idx

		for idx, ch in enumerate(s):
			if ch not in visited:
				while stack and stack[-1] > ch and duple_last[stack[-1]] > idx:
					visited.remove(stack.pop())
				stack.append(ch)
				visited.add(ch)

		return ''.join(stack)
