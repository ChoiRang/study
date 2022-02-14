from encore.addr.vo import Addr

#Dao
class AddrDao:
	def __init__(self):
		self.data = []

	# 추가 메서드
	def insert(self, addr: Addr):
		self.data.append(addr)

	# 검색 메서드
	def search(self, name: str):
		# if str in self.data.name:
		#  	return self.data
		for i in self.data:
			if name == i.name:
				return i
		return

	# 삭제 메서드(
	def delete(self, name: str):
		find_one = self.search(name)
		if find_one is None:
			print('없음!')
		else:
			self.data.remove(find_one)