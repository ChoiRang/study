# 1. 아래와 같이 숫자를 두번 물어보게 하고 * 을 출력해서 사각형을 만드세요

width = input('가로의 숫자를 입력하세요: ')
height = input('세로의 숫자를 입력하세요: ')
star = "*" * int(width)
for height_out in range(0, int(height)):
	print(star)

# 2. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오.

width = input('삼각형의 가로 길이: ')
height = input('삼각형의 세로 길이: ')
result = int(width) * int(height) / 2
print('넓이는: ', result)

# 3. 아래와 같이 별이 찍히게 출력하세요.(중앙정렬 다이아 몬드 형식)

for i in range(0, 6):
	print(f"{'★' * i:^6}")
for i in range(4, 0, -1):
	print(f"{'*' * i:^6}")
# 짝수부분은 정렬안됨

# 4. 1부터 100까지의 수의 합을 계산하던 중에 합이 1000 이상일 때, 최초로 1000을 넘게 하는 수가 무엇인지 코드를 만들고 답을 구하시오

number_list = [x for x in range(1, 101)]
total = 0
for num in number_list:
	total += num
	if total >= 1000:
		print(num)
		break

# 5. 정수를 입력했을때 짝수인지 홀수인지 판별하는 코드를 작성하시오.

number = input('숫자를 입력하세요:')
if int(number) % 2 == 0:
	print('짝수입니다.')
else:
	print('홀수입니다.')

# 6. 리스트 메서드 중 하나를 이용하여 아래의 리스트를 ABCD 순으로 정렳하시오.

namelist = ['Mary', 'Sams', 'Aimy', 'Tom', 'Michale', 'Bob', 'Kelly']
namelist.sort()
print(namelist)

# 7. 주민 등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. (리스트 split과 slice 활용)

citizen_code = input("주빈번호 입력('-'포함): ")
if len(citizen_code) != 14:
	print('주민번호 형식이 아닙니다.')
else:
	code = citizen_code.split('-')[1][:1]
	if code == '1':
		print('남자입니다')
	elif code == '2':
		print('여자압니다.')

# 8. 확장자가 포함된 파일 이름이 담긴 리스트에서 확장자를 제거하고 파일 이름만 추가 리스트에 저장하시오.

file_list = []
file = input('파일이름 임력: ')
file_name = file.split(".")[0]
file_list.append(file_name)
print(file_list)

# 9. 다음 리스트에서 알파벳의 갯수가 7개인 단어를 출력하시오

a = ['alpha', 'bravo', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
for check in a:
	if len(check) == 7:
		print(check)

# 10. 리스트 메서드 중 하나를 이용하여 아래의 리스트에 '화성'이라는 요소를 삽입하시오.
# 출력 전 리스트 planet = ['태양', '수정', '금성', '목성', '토상', '천왕성', '해왕성']
# 출력 후 리스트 planet = ['태양', '수정', '금성', '화성', '목성', '토상', '천왕성', '해왕성']

planet = ['태양', '수정', '금성', '목성', '토상', '천왕성', '해왕성']
print(planet)
planet_index = int(input('넣을 행성 위치:'))
planet_name = input('넣을 행성 이름:')
planet.insert(planet_index, planet_name)
print(planet)

# 11. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 점수를 입력했을때 해당 학점이 출력되게 하시오.
# 81~100: A, 61~80: B, 41~60: C, 21~40: D, 0~20: F

score = int(input('학점 입력: '))
if score > 100:
	print('??')
elif score > 80:
	print('A')
elif score > 60:
	print('B')
elif score > 40:
	print('C')
elif score > 20:
	print('D')
elif score >= 0:
	print('F')
else:
	print('??')

# 12. 최대공약수 및 최소공배수를 구하는 함수를 구현하시오.

num1 = 10
num2 = 12


def gcd(x, y):
	if x < y:
		imsi = x
		x = y
		y = imsi

	while y:
		remain = x % y
		x = y
		y = remain
	return x


def lcm(x, y):
	return x * y // gcd(x, y)


print(gcd(10, 12))
print(lcm(10, 12))


# 13. Card 클래스를 생성해 카드에 충전기능, 소비기능, 잔액을 알려주는 기능을 넣으세요.
# - 충전기능 (charge), 소비기능(consume), print기능(print) # 잔액이 () 원 입니다.

class Card:
	def __init__(self, money):
		self.money = money

	def charge(self, cost):
		self.money = self.money + cost
		return self.money

	def consume(self, cost):
		self.money = self.money - cost
		return self.money

	def __str__(self):
		return f'잔액이 {self.money}원 입니다.'


# 14. 년, 월, 일을 입력하면 그 날이 무슨 요일인지 출력하세요.

import datetime

days = ['월', '화', '수', '목', '금', '토', '일']
date = input('년원일 입력:')
if len(date) != 8:
	print('잘못된 날짜')
else:
	year = int(date[:4])
	month = int(date[4:6])
	day = int(date[6:8])
	# date1 = f'{year}-{month}-{day}'
	date_type = datetime.date(year, month, day)
	week = date_type.weekday()
	print(date_type, days[week])


# 15. 계산이 기능을 하는 Calculator 클래스를 만드세요.
# ex) cal = Calculator()
# in)print(cal.Add(10, 20)), print(cal.Min(10, 20)), print(cal.Mul(10, 20)), print(cal.Div(10, 20))

class Calculator:
	def add(self, num1, num2):
		return num1 + num2

	def min(self, num1, num2):
		return num1 - num2

	def mul(self, num1, num2):
		return num1 * num2

	def div(self, num1, num2):
		return num1 / num2


cal = Calculator()
print(cal.add(10, 20))


# 16. Gorila 라는 클래스를 생성하세요.
# 1) 바나나를 먹는 기능: eat, 2) 바나나가 뱃속에 몇개 남았는지 확인하는 기능: check, 3) 소리지르는 기능: shout, 4) 걷는 기능: walk

class Gorila:
	def __init__(self):
		self.banana = 0

	def eat(self):
		self.banana += 1
		return '바나나 먹는다'

	def check(self):
		return f'바나나 배속에 {self.banana} 개 있다'

	def shout(self):
		return '크와앙'

	def waik(self):
		return '뚜벅두벅'


# 17.Gun 이라는 클래스르 생성하시오.
# 1) 충전 기능: charge, 2) 쏘는 기능: shoot, 3) 남아있는 총알 갯수 확인 가능: check

class Gun:
	def __init__(self):
		self.bullets = 0

	def charge(self):
		self.bullets += 30
		return '충전 완료'

	def shoot(self):
		self.bullets -= 1
		return '탕'

	def check(self):
		return f'탄창에{self.bullets}발 남아있다'


# 18. 아직 정렬되지 않은 값을 이미 정렬된 배열 사이에 끼워 넣는 과정을 반복하여 정렬하는 것을 삽입정렬 이라고 합니다.
# 주어진 리스트를 삽입정렬함수(insert_sort)를 생성하여 오름차순으로 정렬하시오.

number_list = [6, 2, 3, 7, 8, 10, 21, 1]


def insert_sort(arr_list):
	for i in range(1, len(arr_list)):
		for j in range(i, 0, -1):
			if arr_list[j] < arr_list[j - 1]:
				arr_list[j], arr_list[j - 1] = arr_list[j - 1], arr_list[j]
			else:
				break
	return arr_list

print(insert_sort(number_list))

# 19. 앞뒤로 이웃한 숫자를 비교하여 크기가 큰 숫자를 작은숫자보닫 앞에 있을 경우 서로 위치를 바꿔 가며 정렬하는 것을 버블정렬이라고 합니다.
# 주어진 리스트를 버블정렬함수(bubble_sort)를 생성하여 오름차순으로 정렬하시오.

number_list = [4, 3, 2, 1, 8, 7, 5, 10, 11, 16, 21, 6]


def bubble_sort(list):
	for i in range(0, len(list) - 1):
		for j in range(i, len(list)):
			if list[i] > list[j]:
				big_number = list[i]
				list[i] = list[j]
				list[j] = big_number
	return list


print(bubble_sort(number_list))

# 20. 팩토리얼은 1부터 n 까지의 연속한 숫자의 곱이다. 팩토리얼을 함수(factorial)로 구현하는데, 재귀함수를 이용하여 구현하시오.

def factorial(n):
	if n > 0:
		return n * factorial(n - 1)
	else:
		return 1


print(factorial(3))
