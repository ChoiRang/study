import pymysql
from python_files.user.user_vo import UserVo

class UserDao:
	def __init__(self):
		self.conn = None

	def connection(self):
		self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='project_db')

	def disconnection(self):
		self.conn.close()

	def insert(self, user_vo: UserVo):
		try:
			self.connection()
			cursor = self.conn.cursor()
			sql = 'insert into user_data(user_id, user_password, nick_name) values(%s, %s, %s)'
			data = (user_vo.user_id, user_vo.user_password, user_vo.nick_name)
			cursor.execute(sql, data)
			self.conn.commit()
		except Exception as e:
			print(e)
		finally:
			self.disconnection()

	def select_by_user_id(self, user_id):
		try:
			self.connection()
			cursor = self.conn.cursor()
			sql = 'select * from user_data where user_id = %s'
			data = (user_id,)
			cursor.execute(sql, data)
			row = cursor.fetchone()
			if row:
				return UserVo(row[0], row[1], row[2], row[3])
		except Exception as e:
			print(e)
		finally:
			self.disconnection()

	def check_user_password(self, user_id, user_password):
		try:
			user_vo = self.select_by_user_id(user_id)
			if user_vo is None:
				return
			else:
				if user_vo.user_password == user_password:
					return user_vo
				else:
					return
		except Exception as e:
			print(e)


