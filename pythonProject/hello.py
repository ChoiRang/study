import random
print('hello')
a = 100

human = "가위"

index = random.randint(0,2)
computer = random.choice(["가위", "바위", "보"])
result = "이겼습니다" if computer == "보" else "졌습니다" if computer == "바위" else "비겼습니다"
print(result)


print("ok")
random.sample(range(1, 46, 1), 3)

#구구단!!!
for first in range(3, 4):
  for second in range(1, 10):
    print(str(first) + "*" + str(second), "=", first*second)

class Calculator:
  def __init__(self):
    self.value = 0
  def add(self, val):
    self.value += val


class UpgradeCalculator(Calculator):
  def add(self, value):
    self.value += 10
  def minus(self, val):
    self.value -= val


class MaxLimitCalculator(Calculator):
  def add(self, value):
    self.value += value
    if self.value > 100:
      self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(70)
print(cal.value)

i = 1
total = 0
while i < 1001:
  if i % 3 == 0:
    total += i
  i = i + 1
print(total)

count = 1
star = "*"
while count < 6:
  print(star)
  star = star + "*"
  count += 1

for nums in range(1, 101):
  print(nums)

scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total_score = 0
for score in scores:
  total_score += score
print(total_score / len(scores))

numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

numbers = [1, 2, 3, 4, 5]
result = [number*2 for number in numbers if number % 2 == 1]
print(result)


