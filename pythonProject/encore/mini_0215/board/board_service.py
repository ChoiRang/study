from encore.mini_0215.board.board_dao import BoardDao
from encore.mini_0215.board.board_vo import BoardVo


class BoardService:
	def __init__(self):
		self.dao = BoardDao()

	def insert_board(self, user_id):
		title = input('글 제목:')
		content = input('내용 입력: ')
		self.dao.insert_board(BoardVo(writer=user_id, w_date=0, title=title, content=content))

	def search_by_num(self):
		num = input('글 번호 입력: ')
		board_vo = self.dao.select_num(num)
		if board_vo is None:
			print(num, '번은 없는 번호 입니다.')
		else:
			print(board_vo)

	def search_by_writer(self):
		writer = input('작성자 이름 입력:')
		board_vo = self.dao.select_writer('%' + writer + '%')
		if len(board_vo) == 0:
			print('검색 결과 없습니다.')
		else:
			for find_list in board_vo:
				print(find_list)

	def search_by_title(self):
		title = input('제목 입력:')
		board_vo = self.dao.select_title('%' + title + '%')
		if len(board_vo) == 0:
			print('검색 결과 없습니다.')
		else:
			for find_list in board_vo:
				print(find_list)

	def modify_board(self, user_id):
		num = input('수정할 글 번호 입력하세요: ')
		board_vo = self.dao.select_num(num)
		if board_vo is None:
			print(num, '번은 없는 번호 입니다.')
		elif board_vo.writer != user_id:
			print('글 작성자만 수정할 수 있습니다.')
		else:
			data = []
			s = ['타이틀: ', '내용: ']
			attribute = ['title', 'content']
			for i in range(0, len(s)):
				data.append(input(s[i]))

			for idx, i in enumerate(data):
				if i != '':
					board_vo.__setattr__(attribute[idx], i)
			self.dao.update_board(board_vo, num)

	def delete_board(self, user_id):
		num = input('삭제할 번호를 입력하세요')
		board_vo = self.dao.select_num(num)
		if board_vo is None:
			print(num, '번은 없는 번호 입니다.')
		elif board_vo.writer != user_id:
			print('글 작성자만 삭제할 수 있습니다.')
		else:
			self.dao.delete_board(num)

	def print_all(self):
		print('=====모든 정보 출력=====')
		data = self.dao.select_all()
		for i in data:
			print(i)
