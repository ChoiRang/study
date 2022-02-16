import pymysql
from encore.mini_0215.member.member_vo import MemberVo


class MemberDao:
	def __init__(self):
		self.conn = None

	def connection(self):
		self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='encore_db', charset='utf8')

	def disconnect(self):
		self.conn.close()

	def insert_member(self, member):
		try:
			self.connection()
			cursor = self.conn.cursor()
			sql = 'insert into member(id, pwd, name, email) values(%s, %s, %s, %s)'
			data = (member.id, member.pwd, member.name, member.email)
			cursor.execute(sql, data)
			self.conn.commit()
		except Exception as e:
			print(e)
		finally:
			self.disconnect()

	def select_id(self, id):
		try:
			self.connection()
			cursor = self.conn.cursor()
			sql = 'select * from member where id = %s'
			data = (id, )
			cursor.execute(sql, data)
			row = cursor.fetchone()
			if row:
				return MemberVo(row[0], row[1], row[2], row[3])
		except Exception as e:
			print(e)
		finally:
			self.disconnect()

	def update_member(self, user_vo, id):
		try:
			self.connection()
			cursor= self.conn.cursor()
			sql = 'update member set pwd = %s, name = %s, email = %s where id = %s'
			data = (user_vo.pwd, user_vo.name, user_vo.email, id)
			cursor.execute(sql, data)
			self.conn.commit()
		except Exception as e:
			print(e)
		finally:
			self.disconnect()

	def login_member(self, id, pwd):
		try:
			user_vo = self.select_id(id)
			if user_vo is not None:
				if user_vo.pwd != pwd:
					return
				else:
					return user_vo
		except Exception as e:
			print(e)

	def delete_member(self, id, pwd):
		try:
			user_vo = self.select_id(id)
			if user_vo.pwd != pwd:
				return False
			else:
				self.connection()
				cursor = self.conn.cursor()
				sql = 'delete from member where id = %s'
				data = (id, )
				cursor.execute(sql, data)
				self.conn.commit()
				self.disconnect()
				return True
		except Exception as e:
			print(e)
