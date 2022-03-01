from python_files.user.user_dao import UserDao


class UserService:
	def __init__(self):
		self.user_dao = UserDao()

	def sign_user(self, user_vo):
		return self.user_dao.insert(user_vo)

	def id_check(self, user_id):
		check = self.user_dao.select_by_user_id(user_id)
		if check is None:
			return 1
		else:
			return 0

	def login_user(self, user_id, user_password):
		return self.user_dao.check_user_password(user_id, user_password)