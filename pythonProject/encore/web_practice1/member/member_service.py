from encore.web_practice1.member.member_dao import MemberDao
from encore.web_practice1.member.member_vo import MemberVo


class MemberService:
	def __init__(self):
		self.dao = MemberDao()

	def insert_user(self, member_vo):
		self.dao.insert_member(member_vo)

	def login(self, id, pwd):
		user_vo = self.dao.login_member(id, pwd)
		return user_vo

	def get_my_info(self, user_id):
		user_vo = self.dao.select_id(user_id)
		return user_vo

	def modify_user(self, user_vo, user_id):
		self.dao.update_member(user_vo, user_id)

	def print_my_info(self, user_id):
		user_vo = self.dao.select_id(user_id)
		print(user_vo)

	def resign_user(self, id):
		done = self.dao.delete_member(id)
		return done
