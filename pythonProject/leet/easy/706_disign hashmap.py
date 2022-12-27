class MyHashMap:

	def __init__(self):
		self.hash_map = dict()

	def put(self, key: int, value: int) -> None:
		self.hash_map[key] = value

	def get(self, key: int) -> int:
		if key in self.hash_map.keys():
			return self.hash_map[key]
		else:
			return -1

	def remove(self, key: int) -> None:
		self.hash_map.pop(key, None)
