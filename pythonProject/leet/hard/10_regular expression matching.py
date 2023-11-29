class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		cache = {}
		len_s, len_p = len(s), len(p)

		def dfs(i, j):
			if (i, j) in cache:
				return cache[(i, j)]
			if i >= len_s and j >= len_p:
				return True
			if j >= len_p:
				return False

			match = i < len_s and (s[i] == p[j] or p[j] == ".")
			if (j + 1) < len_p and p[j + 1] == "*":
				cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
				return cache[(i, j)]

			if match:
				cache[(i, j)] = dfs(i + 1, j + 1)
				return cache[(i, j)]
			cache[(i, j)] = False
			return False

		return dfs(0, 0)


"""
"." -> 아무 문자 1개
"*" -> 앞의 문자 0~무한 생성 가능(0번: 제거 가능)

i, j 가 끝까지 도달하면 같은 문자열이다.
j 가 먼저 도달하면 i 순회를 끝까지 못 했기에 다른 문자열

"*"은 모든 상황에 대응 가능하기에 가장 먼저 처리해야한다.
"*"이 다음문자열에 있을 경우 "*"을 사용하거나 사용하지 않는 2가지 분기로 나뉨
	->"*"미사용: dfs(i, j + 2)
						: (s[i] == p[j+2]) ? 1 : 0
	->"*"사용: (match and dfs(i + 1, j))
						: (s[i] == p[j] and s[i+1] == p[j]) ? 1 : 0
	둘 중 하나의 경우만 통과하면 해당(i, j)경우 같은 문자열이다.
	-> s[i] != p[j] ? -> (p[j], p[j+1]) 통으로 제거
	-> s[i] == p[j] ? -> i++ 하며 같은 문자열 찾기
if match: -> 다음값으로 dfs(i+1, j+1)진행, return True ? False
"""

