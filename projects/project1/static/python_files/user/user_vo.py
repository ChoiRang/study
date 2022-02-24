class UserVo:
	def __init__(self, user_index=None, user_id=None, user_password=None, nick_name=None):
		self.user_index = user_index
		self.user_id = user_id
		self.user_password = user_password
		self.nick_name = nick_name

	def __str__(self):
		return f'user id: {self.user_id} /password: {self.user_password} /nick_name: {self.nick_name}'


