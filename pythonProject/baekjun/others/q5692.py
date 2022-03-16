from sys import stdin
from math import factorial

while True:
	number = stdin.readline().rstrip()
	number_len = len(number)
	decimal_number = 0

	if number == '0':
		break

	for i in range(number_len):
		decimal_number += int(number[i]) * factorial(number_len-i)

	print(decimal_number)
