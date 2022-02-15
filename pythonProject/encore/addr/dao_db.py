import pymysql
from encore.addr.vo import Addr


class AddrDaoDB:
	def __init__(self):
		self.conn = None

	def connect(self):
		self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='encore_db', charset='utf8')

	def disconnect(self):
		self.conn.close()

	def insert(self, addr: Addr):
		# 1. db 커넥션 수집
		self.connect()
		# 2. 사용할 cursor객체 생성
		cursor = self.conn.cursor()
		# 3. 실행할 sql문 정의
		sql = 'insert into address(name, tel, addr) values(%s, %s, %s)'
		# 4. sql 문에 %s를 사용했다면 각 자리에 들어갈 값을 튜플로 정의
		d = (addr.name, addr.tel, addr.addr)
		# 5. sql 실행(실행할 sql, %s매칭한 튜플)
		cursor.execute(sql, d)

		self.conn.commit()
		self.disconnect()

	# 검색 메서드
	def search_by_num(self, num: int):  # PK search, only 1 output
		try:
			self.connect()
			cursor = self.conn.cursor()
			sql = 'select * from address where num = %s'
			d = (num,)
			cursor.execute(sql, d)
			row = cursor.fetchone()			# 현재 커서 위치의 한줄 추출
			if row:
				return Addr(row[0], row[1], row[2], row[3])
		except Exception as e:
			print(e)
		finally:
			self.conn.commit()
			self.disconnect()

	def search_by_name(self, name: str):
		res = []
		try:
			self.connect()
			cursor = self.conn.cursor()
			sql = 'select * from address where name like %s'
			d = (name, )
			cursor.execute(sql, d)
			for row in cursor:
				res.append(Addr(row[0], row[1], row[2], row[3]))
			return res
		except Exception as e:
			print(e)
		finally:
			self.disconnect()

	# 수정 메서드
	def update_addr(self, num: int, name, tel, addr):
		try:
			self.connect()
			cursor = self.conn.cursor()
			sql = 'update address set name = %s, tel = %s, addr = %s where num = %s'
			d = (tel, name, addr, num)
			cursor.execute(sql, d)
			self.conn.commit()
		except Exception as e:
			print(e)
		finally:
			self.disconnect()

	# 삭제 메서드(
	def delete(self, num: int):
		try:
			self.connect()
			cursor = self.conn.cursor()
			sql = 'delete * from address where num = %s'
			d = (num, )
			cursor.execute(sql, d)
			self.conn.commit()
			return '삭제 완료'
		except Exception as e:
			print(e)
		finally:
			self.disconnect()

	def select_all(self):
		res = []
		try:
			self.connect()
			cursor = self.conn.cursor()
			sql = 'select * from address'
			cursor.execute(sql)
			for row in cursor:
				res.append(Addr(row[0], row[1], row[2], row[3]))
			return res
		except Exception as e:
			print(e)
		finally:
			self.disconnect()

	# ex
	# 번호(id), 이름(pwd)
