from math import sqrt

n = int(input())
numbers = list(map(int, input().split()))
prime_count = 0
for i in numbers:
	prime = True
	if i < 2:
		continue
	for j in range(2, int(sqrt(i)+1)):
		if i % j == 0:
			prime = False
			break
	if prime is True:
		prime_count += 1
print(prime_count)
