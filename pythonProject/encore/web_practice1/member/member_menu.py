from encore.mini_0215.member.member_service import MemberService


class Menu:
	def __init__(self):
		self.member_service = MemberService()

	def menu(self, check, user_id=None):
		if check == 1:
			login_info = self.member_service.login()
			if login_info is None:
				print('아이디랑 패스워드가 다릅니다')
				return
			else:
				return login_info
		elif check == 8:
			while True:
				print('===유저 관리 메뉴===')
				check1 = int(input('1.정보 수정, 2. 내 정보, 3.회원 탈퇴, 4.뒤로 가기'))
				if check1 == 1:
					self.member_service.modify_user(user_id)
				elif check1 == 2:
					self.member_service.print_my_info(user_id)
				elif check1 == 3:
					done = self.member_service.resign_user(user_id)
					if done:
						print('탈퇴 완료')
						return 1
						break
					else:
						print('비밀번호가 틀립니다.')
				elif check1 == 4:
					break
				else:
					print('없는 번호입니다')
		elif check == 9:
			while True:
				print('===유저 관리 메뉴===')
				check1 = int(input('1.회원가입, 2.뒤로가기'))
				if check1 == 1:
					self.member_service.insert_user()
					print('가입 완료!')
					break
				elif check1 == 2:
					break
				else:
					print('없는 번호입니다')
		else:
			print('없는 번호입니다')
