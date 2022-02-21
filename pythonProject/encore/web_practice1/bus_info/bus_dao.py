import pymysql

class BusDao:
	def __init__(self):
		self.conn = None

	def connection(self):
		self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='encore_db', charset='utf8')

	def disconnect(self):
		self.conn.close()

	def select_by_user_id(self, user_id):
		try:
			self.connection()
			cursor = self.conn.cursor()
			sql = 'select * from user_bus where user_id = %s'
			data = (user_id, )
			cursor.execute(sql, data)
		except Exception as e:
			pass
		finally:
			self.disconnect()

	def duplicate_check(self, user_id, bus_id):
		try:
			self.connection()
			cursor = self.conn.cursor()
			sql = 'select * from user_bus where user_id = %s and bus_code = %s'
			data = (user_id, bus_id)
			cursor.execute(sql, data)
			res = []
			for row in cursor:
				res.append(row)					# imsi
			return res
		except Exception as e:
			print(e)
		finally:
			self.disconnect()

	def insert_info(self, bus_id, bus_name, user_id):
		try:
			check = self.duplicate_check(user_id, bus_id)
			if check is not None:
				print(check)
				return 0
			else:
				self.connection()
				cursor = self.conn.cursor()
				sql = 'insert into user_bus(user_id, bus_code, bus_name) values(%s, %s, %s)'
				data = (user_id, bus_id, bus_name)
				cursor.execute(sql, data)
				self.conn.commit()
				self.disconnect()
				return 1
		except Exception as e:
			pass
