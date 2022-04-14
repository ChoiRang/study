import math

number = list(map(int, input().split()))
day_up, day_down, stick = number
day = math.ceil((stick-day_up)/(day_up-day_down) + 1)

print(day)
