from encore.addr.dao import AddrDao
from encore.addr.dao_db import AddrDaoDB
from encore.addr.vo import Addr


class AddrService:
	# ex
	# 번호(id), 이름(pwd)
	login_no = 0	# login_no = 0 로그아웃, 1이면 로그인 상태
	# login_id = '' # 로그아웃 상태, 공백문자 아니면 로그인 상태

	def __init__(self):
		self.dao = AddrDaoDB()

	# 추가, name은 중복허용안함
	def add_addr(self):
		print('===추가===')
		name = input('name: ')
		tel = input('tel: ')
		addr = input('addr: ')
		self.dao.insert(Addr(name=name, tel=tel, addr=addr))

	def get_by_num(self):
		print('===번호로 검색===')
		num = input('search num: ')
		addr: Addr = self.dao.search_by_num(num)
		if addr is None:
			print('없는 번호')
		else:
			print(addr)

	# 검색: 검색할 이름을 입력받아서 dao 로 검색한 결과 출력
	def get_by_name(self):
		print('===이름 입력===')
		name = input('search name: ')
		addr: list = self.dao.search_by_name('%' + name + '%')
		if addr is None:
			print('예외 발생.')
		elif len(addr) == 0:
			print('검색결과 없습니다.')
		else:
			for addr_list in addr:
				print(addr_list)

	# 수정
	def modify_addr(self):
		print('===수정===')
		num = input('choose num: ')
		addr: Addr = self.dao.search_by_num(num)
		if addr is None:
			print('없는 번호입니다.')
		else:
			print(addr)
			# 다른 방법
			# name = input('new name: ')
			# tel = input('new tel: ')
			# addr = input('new addr: ')
			data = []
			s = ['new name: ', 'new tel: ', 'new address: ']
			for i in range(0, len(data)):
				data.append(input(s[i]))
			for idx, i in data:
				if i != '':
					addr.__setattr__(s[idx], i)
			self.dao.update_addr(addr)

	# 삭제
	def del_addr(self):
		print('===삭제===')
		num = input('delete num: ')
		result = self.dao.delete(num)
		print(result)

	# 전체출력
	def print_all(self):
		for i in self.dao.select_all():
			print(i)

	# ex
	# 번호(id), 이름(pwd)
	def login(self):
		if AddrService.login_no != 0:
			print('로그인 인증!')
			return

		num = int(input('로그인 번호'))
		a = self.dao.select_all(num)

		if a is None:
			print('없는 회원번호')
			return
		else:
			name = input('로그인 이름: ')
			if name == a.name:
				AddrService.login_no = num		# 로그인 처리
			else:
				print('패스워드(불일치)')

	def print_my_info(self):
		if AddrService.login_no == 0:
			print('로그인 먼저 하시져')
			return

		a = self.dao.select_all(AddrService.login_no)

	def logout(self):
		if AddrService.login_no == 0:
			print('로그인 먼저 하시져')
			return
		AddrService.login_no = 0