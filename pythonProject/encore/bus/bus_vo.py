class BusVo:
	def __init__(self, bus_code=None, bus_route_type=None, start_station=None, end_station=None, term=None):
		self.bus_code = bus_code
		self.bus_route_type = bus_route_type
		self.start_station = start_station
		self.end_station = end_station
		self.term = term

	def __str__(self):
		return f'버스 코드:{self.bus_code}' \
				f' /노선 유형:{self.bus_route_type}' \
				f' /기점:{self.start_station}' \
				f' /종점:{self.end_station}' \
				f' /배차 간격:{self.term}분'
