class MemberVo:
	def __init__(self, id: str = None, pwd: str = None, name: str = None, email: str = None):
		self.id = id
		self.pwd = pwd
		self.name = name
		self.email = email

	def __str__(self):  # java toString(), 객체 설명문
		return 'id: ' + str(self.id) + ', name: ' + self.name + ', email: ' + self.email
