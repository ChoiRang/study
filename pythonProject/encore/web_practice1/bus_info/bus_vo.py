class BusVo:
	def __init__(
			self,
			bus_code=None,
			bus_route_name=None,
			start_station=None,
			end_station=None,
			start_time=None,
			end_time=None,
			term=None
	):
		self.bus_code = bus_code
		self.bus_route_name = bus_route_name
		self.start_station = start_station
		self.end_station = end_station
		self.start_time = start_time
		self.end_time = end_time
		self.term = term

	def __str__(self):
		return f'버스 코드:{self.bus_code}' \
				f' /노선 유형:{self.bus_route_name}' \
				f' /기점:{self.start_station}' \
				f' /종점:{self.end_station}' \
				f' /첫차 시간:{self.start_time}' \
				f' /막차 시간:{self.end_time}' \
				f' /배차 간격:{self.term}분'


class Station:
	def __init__(self, seq=None, station_name=None, direction=None, gps_x=None, gps_y=None):
		self.seq = seq
		self.station_name = station_name
		self.direction = direction
		self.gps_x = gps_x
		self.gps_y = gps_y
