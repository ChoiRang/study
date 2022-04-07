import itertools
import math


def solution(number: str):
	num_arr = [i for i in number]
	arr_permutation = []
	prime_number = []

	for digit in range(1, len(num_arr) + 1):
		arr_permutation += itertools.permutations(num_arr, digit)

	num_list = set([int(("").join(i)) for i in arr_permutation])

	for n in num_list:
		if n < 2:
			continue
		else:
			prime_check = True
			for i in range(2, int(math.sqrt(n) + 1)):
				if n % i == 0:
					prime_check = False
					break
			if prime_check is True:
				prime_number.append(n)

	return len(prime_number)


if __name__ == '__main__':
	print(solution('011'))
