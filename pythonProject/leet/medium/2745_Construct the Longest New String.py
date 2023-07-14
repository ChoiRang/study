class Solution:
	def longestString(self, x: int, y: int, z: int) -> int:
		return 2 * (min(x, y) * 2 + 1 + z) - 2 * (x == y)
