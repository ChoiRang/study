from typing import *


class Solution:
	def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
		vowel = [0]
		result = []
		for word in words:
			if word[0] in "aeiou" and word[-1] in "aeiou":
				vowel.append(vowel[-1] + 1)
			else:
				vowel.append(vowel[-1])

		for l, r in queries:
			result.append(vowel[r+1] - vowel[l])

		return result


"""
vowel: 모음
---
!On^2 + words 리스트 분할 시간으로 인해 시간초과!
queries 가 항상 범위이므로 모음이 좌우끝에 있는 경우가 다음과 같을때
|0011100011| : len(10), total_vowel: 5
0|0012333345| : 리스트
0|00123|      : (l:r -> 0:4)+1, vowel : 3
0    2|33345| : (l:r -> 5:9)+1, vowel : 2
0  1|233334|  : (l:r -> 3:8)+1, vowel = 4-1 : 3
0  1|2333|    : (l:r -> 3:6)+1, vowel = 3-1 : 2
0        |45| : (l:r -> 8:9)+1, vowel = 5-3 : 2
"""
