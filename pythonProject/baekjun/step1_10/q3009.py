dots = []
x = []
y = []
for i in range(3):
	dots.append(list(map(int, input().split())))

for i in range(3):
	dot1, dot2 = dots[i]
	x.append(dot1)
	y.append(dot2)

a = [i for i in x if x.count(i) == 1]
b = [i for i in y if y.count(i) == 1]
print(a[0], b[0])
