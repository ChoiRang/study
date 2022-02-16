from encore.mini_0215.member.member_menu import Menu as MemberMenu
from encore.mini_0215.board.board_menu import Menu as BoardMenu


class MainMenu:
	user_id = ''

	def __init__(self):
		self.member_menu = MemberMenu()
		self.board_menu = BoardMenu()

	def main_menu(self):
		global user_id
		user_id = None

		while True:
			print('===게시판===')
			if user_id is None:
				print('게스트 입니다')
				menu_check = int(input('1.로그인, 2.글 번호로 검색, 3.글 작성자로 검색, 4.타이틀로 검색, 7.글 전제 출력, 8.유저메뉴, 10.종료'))
				if menu_check == 1:
					info = self.member_menu.menu(menu_check)
					if info is not None:
						user_id = info.id
				elif menu_check < 8:
					self.board_menu.menu(menu_check)
				elif menu_check == 8:
					self.member_menu.menu(9)
				elif menu_check == 10:
					break
				else:
					print('없는 번호입니다')
			else:
				print('환영합니다!')
				print(user_id)
				menu_check = int(input('1.글쓰기, 2.글 번호로 검색, 3.글 작성자로 검색, 4.타이틀로 검색, 5.수정, 6.삭제, 7.글 전체 출력, 8.유저메뉴, 9.로그아웃, 10.종료'))
				if menu_check < 8:
					self.board_menu.menu(menu_check, user_id)
				elif menu_check == 8:
					out_check = self.member_menu.menu(menu_check, user_id)
					if out_check == 1:
						user_id = None
				elif menu_check == 9:
					user_id = None
				elif menu_check == 10:
					break
				else:
					print('없는 번호입니다.')
