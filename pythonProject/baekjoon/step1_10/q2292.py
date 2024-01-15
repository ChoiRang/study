room_number = int(input())
room_size = 1
count = 1
while room_number > room_size:
	room_size = room_size + 6*count
	count += 1
print(count)
