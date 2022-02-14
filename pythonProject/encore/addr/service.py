from encore.addr.dao import AddrDao
from encore.addr.vo import Addr

class AddrService:
	def __init__(self):
		self.dao = AddrDao()

	# 추가, name은 중복허용안함
	def add_addr(self):
		print('===추가===')
		while True:
			name = input('name: ')
			if self.dao.search(name) is None:
				break
			else:
				print('중복된 이름입니다.')
		tel = input('tel: ')
		addr = input('addr: ')
		self.dao.insert(Addr(name=name, tel=tel, addr=addr))

	# 검색: 검색할 이름을 입력받아서 dao 로 검색한 결과 출력
	def print_addr(self):
		print('===이름 입력===')
		name = input('search name: ')
		find_data = self.dao.search(name)
		if find_data is None:
			print('없는 이름입니다.')
		else:
			print(find_data)

	# 수정
	def modify_addr(self):
		print('===수정===')
		name = input('edit name: ')
		find_data = self.dao.search(name)
		if find_data is None:
			print('없는 이름입니다.')
		else:
			find_data.tel = input('new tel: ')
			find_data.addr = input('new addr: ')

	# 삭제
	def del_addr(self):
		print('===삭제===')
		name = input('delete name: ')
		self.dao.delete(name)

	# 전체출력
	def print_all(self):
		for i in self.dao.data:
			print(i)