# 참과 거짓
import re


class Solution:
	def solution(self, statements):
		for check in reversed(list(set(statements))):
			if statements.count(check) == check:
				return check

		return -1 if 0 in statements else 0


if __name__ == '__main__':
	sol = Solution()
	a = sol.solution([0, 1, 2, 3])
	b = sol.solution([0])
	print(a, b)
# 문제 설명
# 스미드 교수는 논리 수업을 가르친다. 어느 날 그는 다음과 같은 문장을 칠판에 썼다.
# 이 문장들 중 정확히 a개의 문장이 참이다.
# 이 문장들 중 정확히 b개의 문장이 참이다.
# 이 문장들 중 정확히 c개의 문장이 참이다.
# .
# .
# .
# a, b, c 등은 각각 숫자이다. 그리고 그는 학생들에게 이 중 t몇개의 문장이 참인지 물어보았다.
#
# 주어진 정수 배열 statements에 Smith 교수가 쓴 숫자들이 적혀있다. 모두 몇 개의 문장이 참인지 리턴하시오.
# 만약 가능한 답이 두개 이상이라면 그 중 더 큰 숫자를 반환하여라. 가능한 답이 없다면 -1을 리턴하시오.
#
# 참고 / 제약 사항
# statements는 1개 이상, 50개 이하의 요소를 가지고 있다.
# statements의 각 요소는 0 이상, 50 이하이다.

