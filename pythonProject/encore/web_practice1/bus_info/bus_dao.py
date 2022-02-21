import pymysql
from encore.web_practice1.bus_info.bus_vo import BusVo

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
				res.append(BusVo(row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
			return res
		except Exception as e:
			print(e)
		finally:
			self.disconnect()

	def insert_info(self, user_id, bus_vo, bus_id):
		try:
			for bus in bus_vo:
				if bus.bus_code == bus_id:
					check = self.duplicate_check(user_id, bus_id)
					if len(check) == 1:
						return 0
					else:
						self.connection()
						cursor = self.conn.cursor()
						sql = 'insert into user_bus(user_id, bus_code, bus_name, start_station, end_station, start_time, end_time, term) values(%s, %s, %s, %s, %s, %s, %s, %s)'
						data = (user_id, bus.bus_code, bus.bus_route_name, bus.start_station, bus.end_station, bus.start_time, bus.end_time, bus.term)
						cursor.execute(sql, data)
						self.conn.commit()
						self.disconnect()
						return 1
		except Exception as e:
			pass

	def select_by_user_id(self, user_id):
		try:
			self.connection()
			cursor = self.conn.cursor()
			sql = 'select * from user_bus where user_id = %s'
			data = (user_id, )
			cursor.execute(sql, data)
			res = []
			for row in cursor:
				res.append(BusVo(row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
			return res
		except Exception as e:
			print(e)
		finally:
			self.disconnect()
