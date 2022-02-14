from  encore.addr.service import AddrService

# menu
class Menu:
	def __init__(self):
		self.service = AddrService()

	def run(self):
		while True:
			check = input('1. 추가, 2. 검색, 3. 수정, 4. 삭제, 5. 전체출력, 6. 종료')
			if check == '1':
				self.service.add_addr()
			elif check == '2':
				self.service.print_addr()
			elif check == '3':
				self.service.modify_addr()
			elif check == '4':
				self.service.del_addr()
			elif check == '5':
				self.service.print_all()
			elif check == '6':
				break
			else:
				print('없는 매뉴번호 입니다.')
