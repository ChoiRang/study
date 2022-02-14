a = 19
b = [1, 2, 3]
# for i in b:
#	print(i)

# print(type(a))

# tuple
# 파이썬에선 여러개의 값을 반환할 수 있는대 이때 튜플 형태로 반환된다

c = (1, 2, 3)
d = (1)  # int 타입이 됨 산수의(), 즉 먼저 처리 기호가 됨

# print(c, type(c))
# print(d, type(d))

# dictionary
# json : java script object notation
# 자바 스크립트 에서 객체를 정의하는 방법
# json = [] : 배열, {} : 객체
# ex)
# {'flag' : True}
# [{'name' : 'aaa', 'age' : '12'}]
# 딕셔너리는 json과 호환이 좋다 (서로 변경 가능)
# e = {'키1': 1, '키2': 2, '키3': 3}
# for key in e:
# 	print(key, e[key])

# 함수 정의
'''
def 함수이름(파리미터 리스트):
	실행문
'''


# data의 형태는 list, ->int 리턴값은 int (둘다 타입에 대한 힌트임)
def mysum(data: list) -> int:
	total = 0
	for i in data:
		total += i
	return total


def test1(name: str, age: int, tel: int):
	age += 10
	print(name, age, tel)


# 리스트를[] 하나 파라미터로 받아서, 검색할 숫자
def search(num_list: list, find: int) -> int:
	if find in num_list:
		return num_list.index(find)
	return


def my_input():
	name = input('name : ')
	tel = input('tel: ')
	address = input('addr: ')
	return name, tel, address


class Point:
	cnt = 1  # static 변수, 클래스 변수, 변수들을 공통적으로 가지고 있음, static 메모리에 저장, 유호시간이 가장 길음

	# 그러므로 객체 생성 상관없이 존재한다.

	def __init__(self, x=0, y=0):  # 생성자, java: this 와 동일, 현재 객체, 멤버 변수, heap 에 저장
		# 객체를 생성해야 변수가 생성됨
		self.x = x
		self.y = y

	def print_xy(self):  # 일반 메서드
		print('x: ', self.x)
		print('y: ', self.y)

	# 클래스
	@staticmethod
	def method1():  # 객체 생성과 상관없이 클래스 이름으로 접근가능, 클래스 변수나 메서드만 사용가능
		print('정적 메소드')


# main
if __name__ == '__main__':
	# 여러가지 사용 예시 - search
	list_1 = [1, 2, 3, 4, 5]
	res = search(list_1, 6)
	if res is not None:
		print(res, 'find')
	else:
		print('not found')

	# 리턴타입 여러가지 예시 - my_input
	# res = my_input()
	# print(type(res))
	# for i in res:
	# 	print(i)
	# name, tel, addr = my_input()
	# print(name, tel, addr)
	# print('cnt: ', Point.cnt)
	# p1 = Point(4, 5)
	# p1.print_xy()
	# Point.method1()
	# Point.cnt = 2
	# print('cnt: ', Point.cnt)

	# dao 등등