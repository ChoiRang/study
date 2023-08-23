import itertools


# 322ms / 16.47
class Solution:
	def minimumString(self, a: str, b: str, c: str) -> str:
		def plus_str(s1, s2):
			if s1 in s2: return s2
			if s2 in s1: return s1

			n1 = len(s1)
			best = s1 + s2

			for i in range(len(s1)):
				if s1[i:] == s2[:n1 - i]:
					now = s1 + s2[n1 - i:]
					if len(now) < len(best):
						best = now

			return best

		def diff(now, best):
			if len(now) == len(best):
				for i in range(len(now)):
					if now[i] < best[i]:
						best = now
						break
					elif now[i] > best[i]:
						break
			elif len(now) < len(best):
				best = now

			return best

		best = a + b + c
		for per in itertools.permutations([a, b, c]):
			now1 = plus_str(per[0], per[1])
			now2 = plus_str(per[1], per[2])

			now = plus_str(now1, now2)
			best = diff(now, best)

		return best


# 내부 같은 문자 예외
class Solution2:
	def minimumString(self, a: str, b: str, c: str) -> str:
		def plus_str(s1, s2):
			n1 = len(s1)
			best = s1 + s2

			for i in range(len(s1)):
				if s1[i:] == s2[:n1 - i]:
					now = s1 + s2[n1 - i:]
					if len(now) < len(best):
						best = now
			return best

		def diff(now, best):
			if len(now) == len(best):
				for i in range(len(now)):
					if now[i] < best[i]:
						best = now
						break
					elif now[i] > best[i]:
						break
			elif len(now) < len(best):
				best = now
			return best

		best = a + b + c
		for per in itertools.permutations([a, b, c]):
			now1 = plus_str(per[0], per[1])
			now2 = plus_str(per[1], per[2])

			now = plus_str(per[0], now2)
			best = diff(now, best)
			now = plus_str(now1, per[2])
			best = diff(now, best)

		return best


# 뒤로 붙이는 것만 가능한 코드
class Solution1:
	def minimumString(self, a: str, b: str, c: str) -> str:
		def plus_str(arr):
			s1, s2, s3 = arr
			n1 = len(s1)
			best = s1 + s2

			for i in range(len(s1)):
				if s1[i:] == s2[:n1 - i]:
					now = s1 + s2[n1 - i:]
					if len(now) < len(best):
						best = now

			best2 = best + s3
			nb = len(best)

			for i in range(len(best)):
				if best[i:] == s3[:nb - i]:
					now = best + s3[nb - i:]
					if len(now) < len(best2):
						best2 = now
			return best2

		best = a + b + c
		for per in itertools.permutations([a, b, c]):
			now = plus_str(per)
			if len(now) == len(best):
				for i in range(len(now)):
					if now[i] < best[i]:
						best = now
						break
					elif now[i] > best[i]:
						break
			elif len(now) < len(best):
				best = now

		return best


"""
!!! -> [cab], [a], [b] => 답: [cab]
!!! -> [a], [a], [cac] => 답: [cac]
Solution1 => [acab]
Solution2 => [acac]
"""
