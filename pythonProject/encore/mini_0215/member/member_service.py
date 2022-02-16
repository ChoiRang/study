from encore.mini_0215.member.member_dao import MemberDao
from encore.mini_0215.member.member_vo import MemberVo


class MemberService:
	def __init__(self):
		self.dao = MemberDao()

	def insert_user(self):
		id = input('id : ')
		pwd = input('password: ')
		name = input('name: ')
		email = input('email: ')
		self.dao.insert_member(MemberVo(id=id, pwd=pwd, name=name, email=email))

	def login(self):
		id = input('id: ')
		pwd = input('password: ')
		login_info = self.dao.login_member(id, pwd)
		return login_info

	def modify_user(self, user_id):
		user_vo = self.dao.select_id(user_id)
		data = []
		s = ['변경할 비밀번호: ', '변경할 이름:', '변경할 이메일: ']
		attribute = ['pwd', 'name', 'email']
		for i in range(0, len(s)):
			data.append(input(s[i]))

		for idx, i in enumerate(data):
			if i != '':
				user_vo.__setattr__(attribute[idx], i)
		self.dao.update_member(user_vo, user_id)

	def print_my_info(self, user_id):
		user_vo = self.dao.select_id(user_id)
		print(user_vo)

	def resign_user(self, id):
		pwd = input('비밀번호 입력: ')
		done = self.dao.delete_member(id, pwd)
		return done
