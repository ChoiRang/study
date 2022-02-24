from static.python_files.user.user_dao import UserDao


class UserService:
	def __init__(self):
		self.user_dao = UserDao()

	def sign_user(self, user_vo):
		return self.user_dao.insert(user_vo)

