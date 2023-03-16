def solution(sequence):
	s1, s2 = [], []
	frag = 1
	for idx, seq in enumerate(sequence):
		s1.append(seq * frag)
		s2.append(seq * frag * -1)
		frag *= -1
	max_val = 0
	val1, val2 = 0, 0
	for n1, n2 in zip(s1, s2):
		val1 += n1
		val2 += n2
		if val1 < 0: val1 = 0
		if val2 < 0: val2 = 0
		max_val = max(max_val, val1, val2)

	return max_val
