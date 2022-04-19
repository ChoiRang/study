number = int(input())

line = 0
line_end = 0
line_start = 0
while line_end < number:
	line += 1
	line_start = line_end
	line_end += line

array_location = line_end - number
array_total = line_end - line_start
if line % 2 == 0:
	top = array_total - array_location
	down = (array_total + 1) - top
	print(f'{top}/{down}')
else:
	down = array_total - array_location
	top = (array_total+1) - down
	print(f'{top}/{down}')
