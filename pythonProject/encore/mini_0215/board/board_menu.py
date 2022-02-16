from encore.mini_0215.board.board_service import BoardService


class Menu:
	def __init__(self):
		self.board_service = BoardService()

	def menu(self, check, user_id=None):
		if check == 1:
			self.board_service.insert_board(user_id)
		elif check == 2:
			self.board_service.search_by_num()
		elif check == 3:
			self.board_service.search_by_writer()
		elif check == 4:
			self.board_service.search_by_title()
		elif check == 5:
			self.board_service.modify_board(user_id)
		elif check == 6:
			self.board_service.delete_board(user_id)
		elif check == 7:
			self.board_service.print_all()
