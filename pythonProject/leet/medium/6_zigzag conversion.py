class Solution:
	def convert(self, s: str, numRows: int) -> str:
		if numRows == 1:
			return s

		rows = [[] for _ in range(numRows)]
		row = 0
		reverse_row = False
		for s_ch in s:
			rows[row].append(s_ch)

			if reverse_row:
				row -= 1
			else:
				row += 1

			if row % (numRows - 1) == 0:
				reverse_row = not reverse_row

		result = ["".join(row) for row in rows]

		return "".join(result)
