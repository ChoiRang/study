class BoardVo:
	def __init__(self, num=0, writer=None, w_date=None, title=None, content=None):
		self.num = num
		self.writer = writer
		self.w_date = w_date
		self.title = title
		self.content = content

	def __str__(self):
		return '번호: ' + str(self.num) + ', 작성자: ' + self.writer + ', 작성일: ' + self.w_date + ', 제목: ' + self.title + ', 내용: ' + self.content
	