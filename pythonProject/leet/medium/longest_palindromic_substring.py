class Solution:
	def longest_palindrome(self, s: str) -> str:
		def expend(left: int, right: int) -> str:
			while left >= 0 and right < len(s) and s[left] == s[right]:
				left -= 1
				right += 1
			return s[left + 1: right]

		if len(s) < 2 or s == s[::-1]:
			return s

		answer = ''
		for i in range(len(s) - 1):
			answer = max(answer, expend(i, i + 1), expend(i, i + 2), key=len)

		return answer

# max(key=len): 문자열의 길이가 가장 큰것(길이가 같을 경우 인덱스가 가장 작은것)
# 시작 위치 (i=0, +1)를 기준 s[left] == s[right] = True 일 경우 좌우로 확장 하면서 끝을 비교하는 형태
# False 일 경우 반환값이 빈값(left+1) 또는 이전의 True 값을 반환
