from encore.addr.service import AddrService

# menu
class Menu:
	def __init__(self):
		self.service = AddrService()

	def run(self):
		while True:
			check = input('1. 추가, 2. 번호로 검색, 3. 이름으로 검색, 4. 수정, 5. 삭제, 6. 전체출력, 7. 종료')
			if check == '1':
				self.service.add_addr()
			elif check == '2':
				self.service.get_by_num()
			elif check == '3':
				self.service.get_by_name()
			elif check == '4':
				self.service.modify_addr()
			elif check == '5':
				self.service.print_all()
			elif check == '6':
				self.service.print_all()
			elif check == '7':
				break
			else:
				print('없는 매뉴번호 입니다.')
