from datetime import datetime
from encore.mini_0215.board.board_vo import BoardVo
import pymysql


class BoardDao:
	def __init__(self):
		self.conn = None

	def connection(self):
		self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='encore_db', charset='utf8')

	def disconnect(self):
		self.conn.close()

	def insert_board(self, board):
		try:
			self.connection()
			cursor = self.conn.cursor()
			sql = 'insert into board(writer, w_date, title, content) values(%s, %s, %s, %s)'
			current_time = datetime.today()
			data = (board.writer, current_time, board.title, board.content)
			cursor.execute(sql, data)
			self.conn.commit()
		except Exception as e:
			print(e)
		finally:
			self.disconnect()

	def select_num(self, num):
		try:
			self.connection()
			cursor = self.conn.cursor()
			sql = 'select * from board where num = %s'
			data = (num, )
			cursor.execute(sql, data)
			row = cursor.fetchone()
			if row:
				return BoardVo(row[0], row[1], str(row[2]), row[3], row[4])
		except Exception as e:
			print(e)
		finally:
			self.disconnect()

	def select_writer(self, writer):
		res = []
		try:
			self.connection()
			cursor = self.conn.cursor()
			sql = 'select * from board where writer like %s'
			data = (writer, )
			cursor.execute(sql, data)
			for row in cursor:
				res.append(BoardVo(row[0], row[1], str(row[2]), row[3], row[4]))
			return res
		except Exception as e:
			print(e)
		finally:
			self.disconnect()

	def select_title(self, title):
		res = []
		try:
			self.connection()
			cursor = self.conn.cursor()
			sql = 'select * from board where title like %s'
			data = (title, )
			cursor.execute(sql, data)
			for row in cursor:
				res.append(BoardVo(row[0], row[1], str(row[2]), row[3], row[4]))
			return res
		except Exception as e:
			print(e)
		finally:
			self.disconnect()

	def update_board(self, board_vo, num):
		try:
			self.connection()
			cursor = self.conn.cursor()
			sql = 'update board set w_date = %s, title = %s, content = %s where num = %s'
			current_time = datetime.today()
			data = (current_time, board_vo.title, board_vo.content, num)
			cursor.execute(sql, data)
			self.conn.commit()
		except Exception as e:
			print(e)
		finally:
			self.disconnect()

	def delete_board(self, num):
		try:
			self.connection()
			cursor = self.conn.cursor()
			sql = 'delete from board where num = %s'
			data = (num, )
			cursor.execute(sql, data)
			self.conn.commit()
		except Exception as e:
			print(e)
		finally:
			self.disconnect()

	def select_all(self):
		res = []
		try:
			self.connection()
			cursor = self.conn.cursor()
			sql = 'select * from board order by num'
			cursor.execute(sql)
			for row in cursor:
				res.append(BoardVo(row[0], row[1], str(row[2]), row[3], row[4]))
			return res
		except Exception as e:
			print(e)
		finally:
			self.disconnect()
